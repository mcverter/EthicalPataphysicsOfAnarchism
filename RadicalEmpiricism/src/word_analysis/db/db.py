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

def insert_into_table(table, columns, values):
    if table and columns and values:
        sanitized_values = [f"'{sanitize(v)}'" for v in values]
        query = f'''
                INSERT INTO {table} ({",".join(columns)}) 
                VALUES ({",".join(sanitized_values)})
                ON CONFLICT ({columns[0]}) 
                DO NOTHING;
                '''
        execute(query)

def update_table(table, set_column, set_value, where_column, where_value):
    if table and set_column and set_value and where_column and where_value:
        query = f"UPDATE {table} SET {set_column} = '{sanitize(set_value)}' WHERE {where_column}='{sanitize(where_value)}'"
        execute(query)

