import os
import psycopg2
from .sanitize_values import sanitize

DB_PASS = os.environ["DB_PASS"]

conn = psycopg2.connect(database="word_analysis",
                        host="localhost",
                        user="postgres",
                        password=DB_PASS,
                        port="5432")


def get_db_cursor():
    return conn.cursor()


def execute(query):
    cursor = get_db_cursor()
    cursor.execute(query)

def commit_all():
    conn.commit()


def select_from_table(table, columns):
    if table and columns:
        cursor = get_db_cursor()
        query = f'SELECT ({",".join(columns)}) from {table}'
        cursor.execute(query)
        return cursor.fetchall()


def check_for_value(table, select_col, where_col, where_val):
    cursor = get_db_cursor()
    query = f'SELECT {select_col} from {table} where {where_col} = {where_val}'
    cursor.execute(query)
    result = cursor.fetchone()
    print(result)
    return result


def update_foreign_key(main_table,
                       fk_table,
                       main_where_col,
                       main_where_val,
                       main_fk_col,
                       fk_where_col,
                       fk_where_value):
    fk_id = check_for_value(fk_table,
                            'id',
                            fk_where_col,
                            fk_where_value)
    if fk_id is None:
        fk_id = insert_into_table(fk_table,
                                  fk_where_col,
                                  fk_where_value)
    update_table(main_table,
                 main_fk_col,
                 fk_id,
                 main_where_col,
                 main_where_val)


def insert_into_table(table, columns, values):
    if table and columns and values:
        sanitized_values = [f'{v}' if isinstance(v, int) else f"'{sanitize(v)}'" for v in values]
        print(sanitized_values)
        query = f'''
                INSERT INTO {table} ({",".join(columns)}) 
                VALUES ({",".join(sanitized_values)})
                ON CONFLICT ({columns[0]}) 
                DO NOTHING
                RETURNING ID;
                '''
        cursor = get_db_cursor()
        cursor.execute(query)
        result = cursor.fetchone()
        print(result)
        return result


'''
  INSERT INTO word_analysis_word (french,ti,otb) 
                VALUES ('préface',4,2)
                ON CONFLICT (french) 
                DO NOTHING;
                '''


def update_table(table, set_column, set_value, where_column, where_value):
    if table and set_column and set_value and where_column and where_value:
        query = f"UPDATE {table} SET {set_column} = '{sanitize(set_value)}' WHERE {where_column}='{sanitize(where_value)}'"
        execute(query)
