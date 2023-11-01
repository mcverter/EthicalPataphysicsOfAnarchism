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

def select_from_table(table, fields):
    if table and fields:
        cursor = get_db_cursor()
        query = f'SELECT ({",".join(fields)}) from {table}'
        cursor.execute(query)
        return cursor.fetchall()

def insert_into_table(table, fields, values):
    if table and fields and values:
        sanitized_values = [f"'{sanitize(v)}'" for v in values]
        query = f'''
                INSERT INTO {table} ({",".join(fields)}) 
                VALUES ({",".join(sanitized_values)})
                ON CONFLICT ({fields[0]}) 
                DO NOTHING;
                '''
        execute(query)

def update_table(table, set_field, set_value, where_field, where_value):
    if table and set_field and set_value and where_field and where_value:
        query = f"UPDATE {table} SET {set_field} = '{sanitize(set_value)}' WHERE {where_field}='{sanitize(where_value)}'"
        execute(query)

