import re
import sqlite3


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

