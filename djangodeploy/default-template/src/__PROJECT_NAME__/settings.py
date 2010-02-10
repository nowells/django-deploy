from djangodeploy import logconfig
from djangodeploy.config import load_config
import os
from simplersa import rsa

CONFIG_IDENTIFIER = os.getenv("CONFIG_IDENTIFIER")

SITE_ROOT = os.path.dirname(os.path.abspath(os.path.realpath(__file__)))
PYTHON_ROOT = os.path.dirname(SITE_ROOT)
PROJECT_ROOT = os.path.dirname(PYTHON_ROOT)
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'var', 'media')

# Setup logging
default_log_path = os.path.join(PROJECT_ROOT, 'etc', 'logging.ini')
specific_log_path = os.path.join(PROJECT_ROOT, 'etc', CONFIG_IDENTIFIER, 'logging.ini')
logconfig.fileConfig([default_log_path, specific_log_path])

# Register default rsa key
rsa.register(os.path.join(PROJECT_ROOT, 'etc', 'key.rsa'))
# Register config rsa key
if os.path.exists(os.path.join(PROJECT_ROOT, 'etc', CONFIG_IDENTIFIER, 'key.rsa')):
    rsa.register(os.path.join(PROJECT_ROOT, 'etc', CONFIG_IDENTIFIER, 'key.rsa'), key=CONFIG_IDENTIFIER)

load_config('settings', os.path.join(PROJECT_ROOT, 'etc'), globals())
load_config('settings', os.path.join(PROJECT_ROOT, 'etc', CONFIG_IDENTIFIER), globals())
