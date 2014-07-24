#!/usr/bin/env python
"""
Raven-django
============

Raven-Django is a Raven extension that provides full out-of-the-box support
for `Django <https://www.djangoproject.com>`_ framework.
Raven itself is a Python client for `Sentry <http://www.getsentry.com/>`_.
"""

# Hack to prevent stupid "TypeError: 'NoneType' object is not callable" error
# in multiprocessing/util.py _exit_function when running `python
# setup.py test` (see
# http://www.eby-sarna.com/pipermail/peak/2010-May/003357.html)
for m in ('multiprocessing', 'billiard'):
    try:
        __import__(m)
    except ImportError:
        pass

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import sys

dev_requires = [
    'flake8>=2.0,<2.1',
]

tests_require = [
    'Django>=1.4',
    'mock',
    'pep8',
    'pytz',
    'pytest',
    'pytest-cov>=1.4',
    'pytest-django',
    'python-coveralls',
]

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


setup(
    name='raven',
    version='0.0.0',
    author='Xavier Ordoquy',
    author_email='xordoquy@linovia.com',
    url='http://github.com/getsentry/raven-django',
    description='Raven-django is a Django extension for Raven (https://www.getsentry.com)',
    long_description=__doc__,
    packages=find_packages(exclude=("tests", "tests.*",)),
    zip_safe=False,
    extras_require={
        'tests': tests_require,
        'dev': dev_requires,
    },
    license='BSD',
    tests_require=tests_require,
    cmdclass={'test': PyTest},
    include_package_data=True,
    entry_points={},
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)
