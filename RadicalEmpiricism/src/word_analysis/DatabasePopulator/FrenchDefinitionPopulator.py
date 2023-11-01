import re
from larousse_api import larousse
from DatabaseUpdater import DatabaseUpdater
from ..constants import TABLE_WORD, COLUMN_FRENCH, TABLE_DEFINITION

OFFSET = 0

def clean_larousse_definition(definition):
    definition = definition.replace('\r\n', ' ')
    definition = definition.replace('\n', ' ')
    definition = definition.replace('\t', ' ')
    definition = definition.replace("'", "''")
    definition = re.sub('Synonymes.*', '', definition)

    return definition

class FrenchDefinitionUpdater(DatabaseUpdater):
    def __init__(self):
        super().__init__(set_table=TABLE_DEFINITION,
                         where_table=TABLE_WORD,
                         set_column=COLUMN_FRENCH,
                         where_column=COLUMN_FRENCH,
                         offset=OFFSET)

    def get_set_value(self, where_value):
        return "; ".join([clean_larousse_definition(c)
             for c in larousse.get_definitions(where_value)])

