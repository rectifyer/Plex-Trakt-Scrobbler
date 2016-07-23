from plugin.models.core import db

from playhouse.apsw_ext import *


def migrate(migrator, database):
    # ActionHistory
    migrator.add_column('action.history', 'part', IntegerField(default=1))

    # ActionQueue
    migrator.add_column('action.queue', 'part', IntegerField(default=1))

#
# Schema specification (for migration verification)
#

SPEC = {
    'action.history': {
        'id':                       'INTEGER PRIMARY KEY NOT NULL',
        'account_id':               'INTEGER NOT NULL',
        'session_id':               'INTEGER',

        'part':                     'INTEGER NOT NULL',
        'rating_key':               'INTEGER',

        'event':                    'VARCHAR(255) NOT NULL',
        'performed':                'VARCHAR(255)',

        'queued_at':                'DATETIME NOT NULL',
        'sent_at':                  'DATETIME NOT NULL'
    },
    'action.queue': {
        'account_id':               'INTEGER NOT NULL',
        'session_id':               'INTEGER PRIMARY KEY',

        'progress':                 'REAL',

        'part':                     'INTEGER NOT NULL',
        'rating_key':               'INTEGER',

        'event':                    'VARCHAR(255) PRIMARY KEY NOT NULL',
        'request':                  'BLOB NOT NULL',

        'queued_at':                'DATETIME NOT NULL',
    },
}
