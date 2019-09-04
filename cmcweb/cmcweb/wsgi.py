"""
WSGI config for cmcweb project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ["DJANGO_SETTINGS_MODULE"] = "cmcweb.settings"
#os.environ['HTTPS'] = "on"
os.environ['CMC_NAME'] = ''
os.environ['CMC_USER'] = ''
os.environ['CMC_PASSWORD'] = ''
os.environ['CMC_HOST'] = ''
os.environ['CMC_PORT'] = ''

_application = get_wsgi_application()

env_variables_to_pass = ['CMC_USER', 'CMC_PASSWORD']
def application(environ, start_response):
    # pass the WSGI environment variables on through to os.environ
    for var in env_variables_to_pass:
        os.environ[var] = environ.get(var, '')
    return _application(environ, start_response)
