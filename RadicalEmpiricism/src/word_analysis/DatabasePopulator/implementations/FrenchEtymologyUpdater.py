from DatabaseUpdater import DatabaseUpdater
from RadicalEmpiricism.src.word_analysis.constants import TABLE_WORD, COLUMN_FRENCH, TABLE_ETYMOLOGY

OFFSET = 0
class FrenchEtymologyUpdater(DatabaseUpdater):
    def __init__(self):
        super().__init__(set_table=TABLE_ETYMOLOGY,
                         where_table=TABLE_WORD,
                         set_column=COLUMN_FRENCH,
                         where_column=COLUMN_FRENCH,
                         offset=OFFSET)

    def get_set_value(self, where_value):
        pass

