import os
import django
from django.utils.encoding import force_str
from .settings import *
django.utils.encoding.force_text = force_str

ALLOWED_HOSTS = [

    "zema-admin-portal.internal.calmgrass-743c6f7f.francecentral.azurecontainerapps.io"]
CSRF_TRUSTED_ORIGINS = [
    "https://zema-admin-portal.internal.calmgrass-743c6f7f.francecentral.azurecontainerapps.io/"]

DATABASES = {
    'default': {},
    'all_other':  {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': "zema_admin",
        'USER': "zemadatabaseadmin",
        'PASSWORD': "StrongP@ssword",
        'HOST': "zema-postgresql-v100.postgres.database.azure.com",
        'PORT': '5432',
        'OPTIONS': {'sslmode': 'disable'}
    },
    'music_db':  {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': "music_database",
        'USER': "zemadatabaseadmin",
        'PASSWORD': "StrongP@ssword",
        'HOST': "zema-postgresql-v100.postgres.database.azure.com",
        'PORT': '5432',
        'OPTIONS': {'sslmode': 'disable'}
    },
    'podcast_db':  {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': "podcast_database",
        'USER': "zemadatabaseadmin",
        'PASSWORD': "StrongP@ssword",
        'HOST': "zema-postgresql-v100.postgres.database.azure.com",
        'PORT': '5432',
        'OPTIONS': {'sslmode': 'disable'}
    },
    'radio_db':  {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': "radio_database",
        'USER': "zemadatabaseadmin",
        'PASSWORD': "StrongP@ssword",
        'HOST': "zema-postgresql-v100.postgres.database.azure.com",
        'PORT': '5432',
        'OPTIONS': {'sslmode': 'disable'}
    }
}

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, '/static/'),
]
AZURE_ACCOUNT_NAME = 'zemastroragev100'
AZURE_ACCOUNT_KEY = 'AFsY2hZVbyYBKisEkRL+toNNJ7yBOzoJ/cruOxurFHnU84vE+Cmloq9S2ZkCxYaxrM5QemPsUiX5+ASt4WEg8w=='
AZURE_CUSTOM_DOMAIN = f'{AZURE_ACCOUNT_NAME}.blob.core.windows.net'
AZURE_LOCATION = 'zemacontainer'
AZURE_CONTAINER = 'zemacontainer'

STATIC_LOCATION = 'static'
STATIC_URL = f'https://{AZURE_CUSTOM_DOMAIN}/{STATIC_LOCATION}/'

STATICFILES_STORAGE = 'storages.backends.azure_storage.AzureStorage'
DEFAULT_FILE_STORAGE = 'core.custom_storage.AzureMediaStorage'
