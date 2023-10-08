import os
import re
import sqlite3

WORDS_TABLE = 'WordAnalysis_word'

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
DB_FILE = os.path.join(DIR_PATH, '../db.sqlite3')
ETYMONLINE_PATH = os.path.join(DIR_PATH, '../data/html/etymonline.html')
FRENCH_ETYMOLOGY_PATH = os.path.join(DIR_PATH, '../data/html/diccionairedesfrancophones.html')

FRENCH_ETYMOLOGY_SITE = 'https://www.dictionnairedesfrancophones.org/form/survivre'
ETYMONLINE_SITE ='https://www.etymonline.com/search?q=+relative'

def update_sql_command(table, setFieldName, setFieldValue, whereFieldName, whereFieldValue):
    setFieldValue = re.sub("'", "''", setFieldValue)
    whereFieldValue = re.sub("'", "''", whereFieldValue)
    if setFieldName and setFieldValue and whereFieldName and whereFieldValue:
        return f"UPDATE {table} SET {setFieldName} = '{setFieldValue}' WHERE {whereFieldName}='{whereFieldValue}';\n"
    else:
        return ''


def update_word_table(setFieldName, setFieldValue, whereFieldName, whereFieldValue):
    return update_sql_command(WORDS_TABLE, setFieldName, setFieldValue, whereFieldName, whereFieldValue)

def get_db_cursor():
    con = sqlite3.connect(DB_FILE)
    return con.cursor()


def select_fields_from_word_table(fields):
    cursor = get_db_cursor()
    joined_fields = "'".join(fields)
    result = cursor.execute(f'SELECT {joined_fields} from {WORDS_TABLE}')
    return result.fetchall()

def add_english_translation():
    pass

def add_english_definition():
    pass

def add_french_definition():
    pass

def add_french_etymology():
    pass

