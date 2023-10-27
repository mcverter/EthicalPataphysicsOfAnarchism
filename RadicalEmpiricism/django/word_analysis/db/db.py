import re
import sqlite3
from ..constants import WORDS_TABLE, DB_FILE

import psycopg2

conn = psycopg2.connect(database="word_analysis",
                        host="localhost",
                        user="postgres",
                        password="SecretPassword",
                        port="5432")


def get_db_cursor():
    # con = sqlite3.connect(DB_FILE)
    return conn.cursor()


def sanitize(value):
    return re.sub("'", "''", value)


def execute_query(query):
    cursor = get_db_cursor()
    cursor.execute(query)
    conn.commit()


def insert_word_into_table(french, ti, otb):
    cursor = get_db_cursor()
    query = f'''
        INSERT INTO {WORDS_TABLE} (french, ti, otb) 
        VALUES ('{sanitize(french)}', {ti}, {otb})
        ON CONFLICT (french) 
        DO NOTHING;
        '''
    return query


def update_word_table(table, setFieldName, setFieldValue, whereFieldName, whereFieldValue):
    query = write_update_sql_command(table, setFieldName, setFieldValue, whereFieldName, whereFieldValue)
    print(query)


def select_fields_from_word_table(fields):
    cursor = get_db_cursor()
    joined_fields = "'".join(fields)
    query = f'SELECT {joined_fields} from {WORDS_TABLE}'
    cursor.execute(query)
    return cursor.fetchall()


def write_update_sql_command(table, setFieldName, setFieldValue, whereFieldName, whereFieldValue):
    setFieldValue = re.sub("'", "''", setFieldValue)
    whereFieldValue = re.sub("'", "''", whereFieldValue)
    if setFieldName and setFieldValue and whereFieldName and whereFieldValue:
        return f"UPDATE {table} SET {setFieldName} = '{setFieldValue}' WHERE {whereFieldName}='{whereFieldValue}';\n"
    else:
        return ''

def commit_all():
    conn.commit()


def update_word_table(setFieldName, setFieldValue, whereFieldName, whereFieldValue):
    query = write_update_sql_command(WORDS_TABLE, setFieldName, setFieldValue, whereFieldName, whereFieldValue)
    cursor = get_db_cursor()
    cursor.execute(query)


def get_value_string_from_content(content, regex_start, regex_end):
    content = content.replace('\n', ' ')
    content = content.replace('\s+', ' ')
    full_regex = f'{regex_start}.*?{regex_end}'
    full_regex_search = re.search(full_regex, content)
    regex_match = full_regex_search.group(0)
    regex_match = re.sub(regex_start, '', regex_match)
    regex_match = re.sub(regex_end, '', regex_match)
    regex_match = re.sub('\s+', ' ', regex_match)
    regex_match = re.sub('^\s+', '', regex_match)
    regex_match = re.sub('<.*?>', '', regex_match)
    regex_match = re.sub('^.*?>\s*', '', regex_match)
    regex_match = re.sub('<.*?$', '', regex_match)
    return regex_match
