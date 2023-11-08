from ....ForeignKeyUpdater import ForeignKeyUpdater
from RadicalEmpiricism.src.word_analysis.constants import TABLE_WORD, COLUMN_ENGLISH, TABLE_DEFINITION

offset = 0
class EnglishDefinitionUpdater(ForeignKeyUpdater):
    def __init__(self):
        super().__init__(table=TABLE_DEFINITION,
                         where_table=TABLE_WORD,
                         set_column=COLUMN_ENGLISH,
                         where_column=COLUMN_ENGLISH,
                         offset=offset)

    def get_set_value_for_main_table(self, where_value):
        pass

