from ....ForeignKeyUpdater import ForeignKeyUpdater
from RadicalEmpiricism.src.word_analysis.constants import TABLE_WORD, COLUMN_ENGLISH, TABLE_ETYMOLOGY

offset = 0

class EnglishEtymologyUpdater(ForeignKeyUpdater):
    def __init__(self):
        super().__init__(set_table=TABLE_ETYMOLOGY,
                         where_table=TABLE_WORD,
                         set_column=COLUMN_ENGLISH,
                         where_column=COLUMN_ENGLISH,
                         offset=offset)

    def get_set_value(self, where_value):
        pass

