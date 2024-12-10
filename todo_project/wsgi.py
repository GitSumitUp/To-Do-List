import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo_project.settings')

application = get_wsgi_application()

print("Using settings module:", os.environ.get('DJANGO_SETTINGS_MODULE'))
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo_project.settings')

try:
    application = get_wsgi_application()
except Exception as e:
    print(f"Failed to get WSGI application: {e}")

print("Using settings module:", os.environ.get('DJANGO_SETTINGS_MODULE'))
