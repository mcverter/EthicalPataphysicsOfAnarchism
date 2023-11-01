import re
from larousse_api import larousse
from DatabaseUpdater import DatabaseUpdater

def clean_larousse_definition(definition):
    definition = definition.replace('\r\n', ' ')
    definition = definition.replace('\n', ' ')
    definition = definition.replace('\t', ' ')
    definition = definition.replace("'", "''")
    definition = re.sub('Synonymes.*', '', definition)

    return definition

class FrenchDefinitionUpdater(DatabaseUpdater):
    def __init__(self):
        super().__init__(table='', set_column='', where_column='', offset='')

    def get_set_value(self, where_value):
        return "; ".join([clean_larousse_definition(c)
             for c in larousse.get_definitions(where_value)])

