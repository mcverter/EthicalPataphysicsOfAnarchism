
import os
import csv
import re
from larousse_api import larousse
from utils import update_word_table

from .zzz_constants import WORD_MAP_PATH, SQL_OUTPUT_FILE
def clean_larousse_definition(definition):
    definition = definition.replace('\r\n', ' ')
    definition = definition.replace('\n', ' ')
    definition = definition.replace('\t', ' ')
    definition = definition.replace("'", "''")
    definition = re.sub('Synonyme.*', '', definition)

    return definition

def populate_french_definition():
    with open(WORD_MAP_PATH) as f:
        with open(SQL_OUTPUT_FILE, "w", encoding="utf-8") as g:
            reader = csv.reader(f)
            output = ''
            for row in reader:
                (french, ti, otb) = (row)
                french_definition = larousse.get_definitions(french)
                if french_definition is not None and french_definition != []:
                    all_definitions = []
                    for definition in french_definition:
                        cleaned_definition = clean_larousse_definition(definition)
                        all_definitions.append(cleaned_definition)
                    joined_definitions = ' '.join(all_definitions)

                    output = update_word_table('french_definition', joined_definitions, 'french', french)
                    g.write(output)
