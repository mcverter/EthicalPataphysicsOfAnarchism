# https://www.merriam-webster.com/dictionary/infinity
# https://www.larousse.fr/dictionnaires/francais/infini/42937
# >>> exec(open('myscript.py').read())
import os
import csv
import re
from larousse_api import larousse

dir_path = os.path.dirname(os.path.realpath(__file__))
word_map_path = os.path.join(dir_path, '../../generated/WordMap.txt')
sql_output_file = os.path.join(dir_path, '../../generated/sql/french_definitions.sql')


def clean_larousse_definition(definition):
    definition = definition.replace('\r\n', ' ')
    definition = definition.replace('\n', ' ')
    definition = definition.replace('\t', ' ')
    definition = definition.replace("'", "''")
    definition = re.sub('Synonyme.*', '', definition)

    return definition


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

                cleaned_french = french.replace("'", "''")

                output = f"UPDATE WordAnalysis_word SET french_definition = '{' '.join(all_definitions)}' WHERE french='{french}';\n"
                g.write(output)

# Print the array containing all defintions of "Fromage"
print(larousse.get_definitions("Fromage"))
