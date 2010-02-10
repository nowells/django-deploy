import os
from djangodeploy.config import load_config

from __PROJECT_NAME__.settings import PROJECT_ROOT

DEBUG = True

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = os.path.join(PROJECT_ROOT, 'var', 'db', 'database.db')

load_config('local_config', PROJECT_ROOT, globals(), required=False)
