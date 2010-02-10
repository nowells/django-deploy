import os
import sys
import site

os.environ['PYTHON_EGG_CACHE'] = '/tmp/.python_eggs'

# Remember original sys.path.
prev_sys_path = list(sys.path)

# The following code initializes the wsgi application with the virtualenv configured properly.
base = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(os.path.abspath(__file__)))))
site_packages = os.path.join(base, 've', 'lib', 'python%s' % sys.version[:3], 'site-packages')
print site_packages
site.addsitedir(site_packages)

# Reorder sys.path so new directories at the front.
new_sys_path = []
for item in list(sys.path):
    if item not in prev_sys_path:
        new_sys_path.append(item)
        sys.path.remove(item)
sys.path[:0] = new_sys_path

# Now we need to configure the actual wsgi application
os.environ['DJANGO_SETTINGS_MODULE'] = '__PROJECT_NAME__.settings'
os.environ['SERVER_IDENTIFIER'] = 'production'

from django.core.handlers.wsgi import WSGIHandler
_application = WSGIHandler()

def application(environ, start_response):
    return _application(environ, start_response)
