from ....ForeignKeyUpdater import ForeignKeyUpdater
from .....constants import TABLE_WORD, COLUMN_ENGLISH, COLUMN_ETYMOLOGY

offset = 0

class EnglishEtymologyUpdater(ForeignKeyUpdater):
    class FrenchEtymologyUpdater(ForeignKeyUpdater):
        super().__init__(table=TABLE_WORD,
                         set_column=COLUMN_ETYMOLOGY,
                         where_column=COLUMN_ENGLISH,
                         offset=offset)

    def get_set_value(self, where_value):
        pass

