#!/usr/bin/env python
import sys
import os

from djangodeploy.deployment import setup_environment
from __PROJECT_NAME__ import settings

try:
    setup_environment(settings.__file__, '../../etc/*/settings.py', True)
except KeyboardInterrupt:
    print ""
    print "Exiting script."
    sys.exit(0)

from django.core import management

if __name__ == "__main__":
    management.execute_manager(settings)
