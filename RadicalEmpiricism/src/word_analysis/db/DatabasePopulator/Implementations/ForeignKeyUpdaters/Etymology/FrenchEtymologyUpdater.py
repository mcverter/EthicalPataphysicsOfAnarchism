from ....ForeignKeyUpdater import ForeignKeyUpdater
from ......constants import TABLE_WORD, COLUMN_FRENCH, COLUMN_ETYMOLOGY, COLUMN_FRENCH_EXPLANATION

offset = 0


class FrenchEtymologyUpdater(ForeignKeyUpdater):
    def __init__(self):
        super().__init__(table=TABLE_WORD,
                         set_column=COLUMN_ETYMOLOGY,
                         where_column=COLUMN_FRENCH,
                         fk_internal_column=COLUMN_FRENCH_EXPLANATION,
                         offset=offset)

    def get_set_value(self, where_value):
        pass
