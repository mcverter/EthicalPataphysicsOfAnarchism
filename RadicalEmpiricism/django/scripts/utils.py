import os
import re
import sqlite3

WORDS_TABLE = 'WordAnalysis_word'
DIR_PATH = os.path.dirname(os.path.realpath(__file__))
ETYMONLINE_PATH = os.path.join(DIR_PATH, './html/etymonline.html')
DB_FILE = os.path.join(DIR_PATH, '../db.sqlite3')

def open_file_relative_to_scripts_dir(relative_path):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(dir_path, relative_path)

def update_sql_command(table, setFieldName, setFieldValue, whereFieldName, whereFieldValue):
    output = f"UPDATE WordAnalysis_word SET {setFieldName} = '{setFieldValue}' WHERE {whereFieldName}='{whereFieldValue}';\n"


def get_db_cursor():
    con = sqlite3.connect(DB_FILE)
    return con.cursor()


def add_english_translation():
    pass

def add_english_definition():
    pass

def add_french_definition():
    pass

def add_french_etymology():
    pass

def add_english_etymology():
    output = ''
    english = 'foo'

    with open(ETYMONLINE_PATH, "r", encoding="utf-8") as f:
        content = f.read()
        content = content.replace('\n', ' ')
        content = content.replace('\s+', ' ')
        etymology_re = '<div class="word__etymology_expand.*?data-more'
        etym_match = re.search(etymology_re, content)
        raw_div = etym_match.group(0)
        raw_div = re.sub('\s+', ' ', raw_div)
        raw_div = re.sub('<.*?>', '', raw_div)
        raw_div = re.sub('<a data-more', '', raw_div)
        raw_div = re.sub('^\s+', '', raw_div)
        output += f"UPDATE WordAnalysis_word SET english_etymology='{raw_div}' WHERE english='{english}';\n"
        print(raw_div)
