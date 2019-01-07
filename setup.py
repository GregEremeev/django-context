from setuptools import find_packages, setup


with open('requirements.txt') as fin:
    REQUIREMENTS = [line.strip() for line in fin if '#' not in line]


with open('README.md') as readme:
    README = readme.read()


setup(
    name='django-context',
    version='0.1.1',
    packages=find_packages(),
    include_package_data=True,
    license='BSD',
    description=(
        'Django app to have an ability to set custom context '
        'in a main application'),
    long_description=README,
    install_requires=REQUIREMENTS,
    url='https://github.com/GregEremeev/django-context',
    author='Greg Eremeev',
    author_email='gregory.eremeev@gmail.com',
    zip_safe=False,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.1',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
