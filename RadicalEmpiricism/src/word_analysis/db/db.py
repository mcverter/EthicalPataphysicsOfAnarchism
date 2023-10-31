import re
import os
from ..constants import TABLE_WORDS
from .sanitize_values import sanitize

DB_PASS = os.environ["DB_PASS"]

import psycopg2

conn = psycopg2.connect(database="word_analysis",
                        host="localhost",
                        user="postgres",
                        password=DB_PASS,
                        port="5432")


def get_db_cursor():
    return conn.cursor()

def execute_single_query(query):
    cursor = get_db_cursor()
    cursor.execute(query)
    conn.commit()


def commit_all():
    conn.commit()

def select_fields_from_word_table(fields):
    cursor = get_db_cursor()
    joined_fields = "'".join(fields)
    query = f'SELECT {joined_fields} from {TABLE_WORDS}'
    cursor.execute(query)
    return cursor.fetchall()


def insert_word_into_table(french, ti, otb):
    query = f'''
        INSERT INTO {TABLE_WORDS} (french, ti, otb) 
        VALUES ('{sanitize(french)}', {ti}, {otb})
        ON CONFLICT (french) 
        DO NOTHING;
        '''
    return query

def write_update_sql_command(table, setFieldName, setFieldValue, whereFieldName, whereFieldValue):
    setFieldValue = re.sub("'", "''", setFieldValue)
    whereFieldValue = re.sub("'", "''", whereFieldValue)
    if setFieldName and setFieldValue and whereFieldName and whereFieldValue:
        return f"UPDATE {table} SET {setFieldName} = '{setFieldValue}' WHERE {whereFieldName}='{whereFieldValue}';\n"
    else:
        return ''

def update_word_table(setFieldName, setFieldValue, whereFieldName, whereFieldValue):
    query = write_update_sql_command(TABLE_WORDS, setFieldName, setFieldValue, whereFieldName, whereFieldValue)
    cursor = get_db_cursor()
    cursor.execute(query)
