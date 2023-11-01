from DatabaseUpdater import DatabaseUpdater
from ..constants import TABLE_WORD, COLUMN_ENGLISH, TABLE_ETYMOLOGY

OFFSET = 0

class EnglishEtymologyUpdater(DatabaseUpdater):
    def __init__(self):
        super().__init__(set_table=TABLE_ETYMOLOGY,
                         where_table=TABLE_WORD,
                         set_column=COLUMN_ENGLISH,
                         where_column=COLUMN_ENGLISH,
                         offset=OFFSET)

    def get_set_value(self, where_value):
        pass

