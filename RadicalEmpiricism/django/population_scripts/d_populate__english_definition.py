# https://www.merriam-webster.com/dictionary/infinity
# https://www.larousse.fr/dictionnaires/francais/infini/42937
# >>> exec(open('myscript.py').read())

import os
from english_dictionary.scripts.read_pickle import get_dict
from utils import select_fields_from_word_table, update_word_table
from zzz_constants import DIR_PATH
def populate_english_definition():
    sql_output_file = os.path.join(DIR_PATH, '../sql/english_definitions.sql')

    english_dict = get_dict()

    english_words = select_fields_from_word_table(["english"])

    for word in english_words:
        definition = english_dict[word[0]]
        output = update_word_table('english_definition', definition, 'english', word[0])
        with open(sql_output_file, "w", encoding="utf-8") as g:
            g.write(output)
