
class AppConfig(object):
    # Database backend, supported mysql and mongo
    database = 'mysql'
    # MySQL settings
    database_settings = {
        'host': 'localhost',
        'user': 'dezi',
        'password': 'dezi',
        'database': 'dezi'
    }

CONF = AppConfig()
