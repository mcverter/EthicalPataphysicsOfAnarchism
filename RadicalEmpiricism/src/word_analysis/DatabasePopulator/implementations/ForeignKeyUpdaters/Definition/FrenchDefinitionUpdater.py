import re
from larousse_api import larousse
from ....ForeignKeyUpdater import ForeignKeyUpdater
from .....constants import TABLE_WORD, COLUMN_DEFINITION, COLUMN_FRENCH

offset = 0

def clean_larousse_definition(definition):
    definition = definition.replace('\r\n', ' ')
    definition = definition.replace('\n', ' ')
    definition = definition.replace('\t', ' ')
    definition = definition.replace("'", "''")
    definition = re.sub('Synonymes.*', '', definition)

    return definition

class FrenchDefinitionUpdater(ForeignKeyUpdater):
    def __init__(self):
        super().__init__(table=TABLE_WORD,
                         set_column=COLUMN_DEFINITION,
                         where_column=COLUMN_FRENCH,
                         fk_internal_column=COLUMN_FRENCH,
                         offset=offset)



    def get_set_value_for_main_table(self, where_value):
        return "; ".join([clean_larousse_definition(c)
             for c in larousse.get_definitions(where_value)])

