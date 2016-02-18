"""
Django applications settings for automation project.
"""
from automation.settings import INSTALLED_APPS

# Application definition

INSTALLED_APPS += [
    'rest_framework',
]

INSTALLED_APPS += [
    # 'app_api',
    'app_messages',
    'account',
]



