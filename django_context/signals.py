import django_context.tools


def request_started_handler(sender, **kwargs):
    django_context.tools.set_request_id()
    django_context.tools.set_request_start_time()


def request_finished_handler(sender, **kwargs):
    django_context.tools.clear_storage()
