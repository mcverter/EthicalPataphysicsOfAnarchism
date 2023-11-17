from ....ForeignKeyUpdater import ForeignKeyUpdater
from ......constants import TABLE_WORD, COLUMN_ENGLISH, COLUMN_ETYMOLOGY, COLUMN_ENGLISH_EXPLANATION

offset = 0

class EnglishEtymologyUpdater(ForeignKeyUpdater):
    class FrenchEtymologyUpdater(ForeignKeyUpdater):
        def __init__(self):
            super().__init__(table=TABLE_WORD,
                             set_column=COLUMN_ETYMOLOGY,
                             where_column=COLUMN_ENGLISH,
                             fk_internal_column=COLUMN_ENGLISH_EXPLANATION,
                             offset=offset)

    def get_set_value(self, where_value):
        pass

