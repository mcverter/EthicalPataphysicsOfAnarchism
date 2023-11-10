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


def select_value(table, select_col, where_col, where_val):
    cursor = get_db_cursor()
    query = f'SELECT {select_col} from {table} where {where_col} = {where_val}'
    cursor.execute(query)
    result = cursor.fetchone()
    print(result)
    return result


def update_foreign_key(main_table,
                       main_set_column,
                       main_where_column,
                       main_where_val,
                       main_fk_col,
                       fk_table,
                       fk_internal_col,
                       data_value):
    if main_where_val is None or main_where_column is None \
        or main_where_val is None or main_fk_col is None \
        or fk_table is None or fk_internal_col is None \
        or main_set_column is None or data_value is None:
        raise Exception("ERROR: you need to define all parameters to update_foreign_key")

    # first check main table for value in column
    fk_id = select_value(table=main_table,
                         select_col=main_set_column,
                         where_col=main_where_column,
                         where_val=main_where_val)


    fk_id = select_value(table=fk_table,
                        select_col='id',
                         where_col=fk_internal_col,
                         where_val=data_value)
    if fk_id is None:
        fk_id = insert_into_table(fk_table,
                                  fk_internal_col,
                                  data_value)
        update_table(table=main_table,
                     set_column=main_fk_col,
                     set_value=fk_id,
                     where_column=main_where_column,
                     where_value=main_where_val)

    else:
        # check table for value
        fk_internal_value = select_value(fk_table,
                                        select_col=fk_internal_col,
                                         where_col='id',
                                         where_val=fk_id)
        if fk_internal_value is None:
            update_table(table=fk_table,
                         set_column=fk_table,
                         set_value=data_value,
                         where_column='id',
                         where_value=data_value)


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
