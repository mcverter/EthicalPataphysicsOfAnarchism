# https://www.merriam-webster.com/dictionary/infinity
# https://www.larousse.fr/dictionnaires/francais/infini/42937
# >>> exec(open('myscript.py').read())
import os
import csv
import re
from larousse_api import larousse
from utils import update_word_table

dir_path = os.path.dirname(os.path.realpath(__file__))
word_map_path = os.path.join(dir_path, '../../generated/word_map.csv')
sql_output_file = os.path.join(dir_path, '../../generated/sql/french_definitions.sql')


def clean_larousse_definition(definition):
    definition = definition.replace('\r\n', ' ')
    definition = definition.replace('\n', ' ')
    definition = definition.replace('\t', ' ')
    definition = definition.replace("'", "''")
    definition = re.sub('Synonyme.*', '', definition)

    return definition

def update_word_tbl__french_definition_sql():
    with open(word_map_path) as f:
        with open(sql_output_file, "w", encoding="utf-8") as g:
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
