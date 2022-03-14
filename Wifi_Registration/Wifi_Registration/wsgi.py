"""
WSGI config for Wifi_Registration project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
import sys
import site

from django.core.wsgi import get_wsgi_application

sys.path.append(r'C:\Users\user\Desktop\wireframe_and_elements\Stored\wifiRegistration\Wifi_Registration')

os.environ['DJANGO_SETTINGS_MODULE'] = 'Wifi_Registration.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Wifi_Registration.settings')

application = get_wsgi_application()