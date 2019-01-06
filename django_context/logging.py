import logging

import django_context.tools


LOGGER = logging.getLogger(__name__)


class ContextFilter(logging.Filter):

    def filter(self, record):
        record.request_id = django_context.tools.get_request_id()
        record.user_id = django_context.tools.get_user_id()
        response_duration = django_context.tools.get_response_duration()
        if response_duration is not None:
            response_duration = '{0:0.6f}s'.format(response_duration)
        record.response_duration = response_duration
        return True
