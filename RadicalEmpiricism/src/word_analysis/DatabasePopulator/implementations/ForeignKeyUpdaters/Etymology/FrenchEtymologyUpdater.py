from RadicalEmpiricism.src.word_analysis.constants import TABLE_WORD, COLUMN_FRENCH, TABLE_ETYMOLOGY
from ....ForeignKeyUpdater import ForeignKeyUpdater

offset = 0
class FrenchEtymologyUpdater(ForeignKeyUpdater):
    def __init__(self):
        super().__init__(set_table=TABLE_ETYMOLOGY,
                         where_table=TABLE_WORD,
                         set_column=COLUMN_FRENCH,
                         where_column=COLUMN_FRENCH,
                         offset=offset)

    def get_set_value(self, where_value):
        pass

