from __future__ import absolute_import

from django.conf import settings
try:
    from django.conf.urls import url, patterns
except ImportError:
    # for Django version less than 1.4
    from django.conf.urls.defaults import url, patterns  # NOQA

from django.http import HttpResponse


def handler404(request):
    return HttpResponse('', status=404)


def handler500(request):
    if getattr(settings, 'BREAK_THAT_500', False):
        raise ValueError('handler500')
    return HttpResponse('', status=500)


urlpatterns = patterns('',
    url(r'^no-error$', 'tests.views.no_error', name='sentry-no-error'),
    url(r'^fake-login$', 'tests.views.fake_login', name='sentry-fake-login'),
    url(r'^trigger-500$', 'tests.views.raise_exc', name='sentry-raise-exc'),
    url(r'^trigger-500-ioerror$', 'tests.views.raise_ioerror', name='sentry-raise-ioerror'),
    url(r'^trigger-500-decorated$', 'tests.views.decorated_raise_exc', name='sentry-raise-exc-decor'),
    url(r'^trigger-500-django$', 'tests.views.django_exc', name='sentry-django-exc'),
    url(r'^trigger-500-template$', 'tests.views.template_exc', name='sentry-template-exc'),
    url(r'^trigger-500-log-request$', 'tests.views.logging_request_exc', name='sentry-log-request-exc'),
)
