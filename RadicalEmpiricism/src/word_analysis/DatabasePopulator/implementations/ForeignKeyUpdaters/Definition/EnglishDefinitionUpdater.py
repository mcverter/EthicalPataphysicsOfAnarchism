from ....ForeignKeyUpdater import ForeignKeyUpdater
from .....constants import TABLE_WORD, COLUMN_DEFINITION, COLUMN_ENGLISH

offset: int = 0
class EnglishDefinitionUpdater(ForeignKeyUpdater):
    def __init__(self):
        super().__init__(table=TABLE_WORD,
                         set_column=COLUMN_DEFINITION,
                         where_column=COLUMN_ENGLISH,
                         fk_internal_column=COLUMN_ENGLISH,
                         offset=offset)

    def get_set_value_for_main_table(self, where_value):
        pass

