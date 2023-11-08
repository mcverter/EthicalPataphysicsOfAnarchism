from ....SameTableUpdater import SameTableUpdater
from ....constants import TABLE_WORD, COLUMN_FRENCH, TABLE_ETYMOLOGY

offset = 0
class FrenchEtymologyUpdater(SameTableUpdater):
    def __init__(self):
        super().__init__(set_table=TABLE_ETYMOLOGY,
                         where_table=TABLE_WORD,
                         set_column=COLUMN_FRENCH,
                         where_column=COLUMN_FRENCH,
                         offset=offset)

    def get_set_value(self, where_value):
        pass

