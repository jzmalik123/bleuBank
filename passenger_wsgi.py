import imp
import os
import sys


sys.path.insert(0, os.path.dirname(__file__))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bleuBank.settings')
wsgi = imp.load_source('wsgi', 'bleuBank/wsgi.py')
application = wsgi.application
