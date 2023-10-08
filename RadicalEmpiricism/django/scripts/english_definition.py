import os
import re
from english_dictionary.scripts.read_pickle import get_dict
from utils import get_db_cursor, DB_FILE, DIR_PATH

sql_output_file = os.path.join(DIR_PATH, '../sql/english_definitions.sql')

english_dict = get_dict()

cur = get_db_cursor()
res = cur.execute("SELECT english FROM WordAnalysis_word")
english_words = res.fetchall()

output = ''
for word in english_words:
    w = word[0]
    try:
        definition = english_dict[w]
        if definition and w:
            definition = re.sub("'", "''", definition)
            w = re.sub("'", "''", w)
            output += f"UPDATE WordAnalysis_word SET english_definition='{definition}' WHERE english='{w}';\n"
    except:
        print ('an error occurred')
        pass

with open(sql_output_file, "w", encoding="utf-8") as g:
    g.write(output)
