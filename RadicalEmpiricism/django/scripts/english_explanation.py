import sqlite3
import os
import re
from english_dictionary.scripts.read_pickle import get_dict

dir_path = os.path.dirname(os.path.realpath(__file__))
db_file = os.path.join(dir_path, '../db.sqlite3')
sql_output_file = os.path.join(dir_path, '../sql/english_explanations.sql')

english_dict = get_dict()

con = sqlite3.connect(db_file)
cur = con.cursor()
res = cur.execute("SELECT english FROM WordAnalysis_word")
english_words = res.fetchall()

output = ''
for word in english_words:
    w = word[0]
    try:
        explanation = english_dict[w]
        if explanation and w:
            explanation = re.sub("'", "''", explanation)
            w = re.sub("'", "''", w)
            output += f"UPDATE WordAnalysis_word SET english_explanation='{explanation}' WHERE english='{w}';\n"
    except:
        print ('an error occurred')
        pass

with open(sql_output_file, "w", encoding="utf-8") as g:
    g.write(output)
