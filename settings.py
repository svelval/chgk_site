import os

from chgk.database import CommonDatabase


DATABASES_INFO = {
    'common': {
        'name': os.getenv('CHGK_SITE_DB_NAME', ''),
        'user': os.getenv('DB_USER'),
        'password': os.getenv('DB_PASSWORD', '')
    },
    'default': 'common',
}
MIGRATIONS_TABLE_INFO = DATABASES_INFO['common']

db = CommonDatabase(DATABASES_INFO['common']['name'],
                    user=DATABASES_INFO['common']['user'],
                    password=DATABASES_INFO['common']['password'])
