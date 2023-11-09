from .....constants import TABLE_WORD, COLUMN_FRENCH, COLUMN_ETYMOLOGY
from ....ForeignKeyUpdater import ForeignKeyUpdater

offset = 0
class FrenchEtymologyUpdater(ForeignKeyUpdater):
    super().__init__(table=TABLE_WORD,
                     set_column=COLUMN_ETYMOLOGY,
                     where_column=COLUMN_FRENCH,
                     fk_internal_column=COLUMN_FRENCH,
                     offset=offset)

    def get_set_value(self, where_value):
        pass

