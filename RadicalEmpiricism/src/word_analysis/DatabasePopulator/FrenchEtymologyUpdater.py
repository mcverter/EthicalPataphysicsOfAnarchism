from DatabaseUpdater import DatabaseUpdater
from ..constants import TABLE_WORD, COLUMN_FRENCH

OFFSET = 0
class FrenchEtymologyUpdater(DatabaseUpdater):
    def __init__(self):
        super().__init__(table=TABLE_WORD,
                         set_column='',
                         where_column=COLUMN_FRENCH,
                         offset=OFFSET)

    def get_set_value(self, where_value):
        pass

