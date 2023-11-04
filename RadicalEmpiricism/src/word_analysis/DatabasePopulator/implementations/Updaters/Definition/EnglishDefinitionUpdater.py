from ....DatabaseUpdater import DatabaseUpdater
from RadicalEmpiricism.src.word_analysis.constants import TABLE_WORD, COLUMN_ENGLISH, TABLE_DEFINITION

OFFSET = 0
class EnglishDefinitionUpdater(DatabaseUpdater):
    def __init__(self):
        super().__init__(set_table=TABLE_DEFINITION,
                         where_table=TABLE_WORD,
                         set_column=COLUMN_ENGLISH,
                         where_column=COLUMN_ENGLISH,
                         offset=OFFSET)

    def get_set_value(self, where_value):
        pass

