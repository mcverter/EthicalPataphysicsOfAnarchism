import os
from english_dictionary.scripts.read_pickle import get_dict
from utils import DIR_PATH, select_fields_from_word_table, update_word_table

def update_word_tbl__english_definition_sql():
    sql_output_file = os.path.join(DIR_PATH, '../sql/english_definitions.sql')

    english_dict = get_dict()

    english_words = select_fields_from_word_table(["english"])

    output = ''
    for word in english_words:
        definition = english_dict[word[0]]
        output += update_word_table('english_definition', definition, 'english', word[0])

    with open(sql_output_file, "w", encoding="utf-8") as g:
        g.write(output)
