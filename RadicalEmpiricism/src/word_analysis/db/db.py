import psycopg2

from .sanitize_values import sanitize
from .logger import log_insert, log_update_same_table, log_update_fk_table
from ...constants import DB_NAME, DB_PORT, DB_RUNTIME_USER, DB_RUNTIME_PASSWORD, DB_RUNTIME_HOST

DB_RUNTIME_HOST = DB_RUNTIME_HOST[0]  # TODO: fix this

conn = psycopg2.connect(database=DB_NAME,
                        host=DB_RUNTIME_HOST,
                        user=DB_RUNTIME_USER,
                        password=DB_RUNTIME_PASSWORD,
                        port=DB_PORT)


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

'''
select word_analysis_definition.id from  word_analysis_definition 
where word_analysis_definition.english_explanation = 'foo'
'''

def select_single_value(table, select_col, where_col, where_val):
    cursor = get_db_cursor()
    query = f"SELECT {select_col} from {table} where {where_col} = '{sanitize(where_val)}'"
    cursor.execute(query)
    result = cursor.fetchone()
    return result

def get_fk_value_from_main_main_table(main_table,
                                      main_set_column,
                                      main_where_column,
                                      main_where_val ):
    main_fk_value = select_single_value(table=main_table,
                                        select_col=main_set_column,
                                        where_col=main_where_column,
                                        where_val=main_where_val)

    main_fk_value = main_fk_value[0]
    return main_fk_value


def update_foreign_key(main_table,
                       main_set_column,
                       main_where_column,
                       main_where_val,
                       fk_table,
                       fk_internal_column,
                       data_value):
    if main_where_val is None or main_where_column is None \
            or main_where_val is None \
            or fk_table is None or fk_internal_column is None \
            or main_set_column is None or data_value is None:
        raise Exception("ERROR: you need to define all parameters to update_foreign_key")

    log_update_fk_table(main_table, main_set_column, main_where_column, fk_table, fk_internal_column)

    fk_id = get_fk_value_from_main_main_table(main_table, main_set_column, main_where_column, main_where_val)
    if fk_id is None:
        fk_id = insert_into_table(fk_table,
                                  columns=(fk_internal_column,),
                                  values=(data_value,))
        fk_id = fk_id[0]
        update_table(table=main_table,
                     set_column=main_set_column,
                     set_value=fk_id,
                     where_column=main_where_column,
                     where_value=main_where_val)

    else:
        # check table for value
        fk_internal_value = select_single_value(fk_table,
                                                select_col=fk_internal_column,
                                                where_col='id',
                                                where_val=fk_id)
        if fk_internal_value[0] is None:
            update_table(table=fk_table,
                         set_column=fk_internal_column,
                         set_value=data_value,
                         where_column='id',
                         where_value=fk_id)


def no_unique_violation(table, columns, values):
    # TODO: fix unique logic
    unique_column = columns[0]
    unique_value = values[0]
    single_result = select_single_value(table, unique_column, unique_column, unique_value)
    if single_result is None:
        return True
    return False


def insert_into_table(table, columns, values):
    log_insert(table, columns, values)

    if table and columns and values:
        if no_unique_violation(table, columns, values):
            sanitized_values = [f'{v}' if isinstance(v, int) else f"'{sanitize(v)}'" for v in values]
            query = f'''
                    INSERT INTO {table} ({",".join(columns)}) 
                    VALUES ({",".join(sanitized_values)})
    /*              ON CONFLICT ({columns[0]})  
                    DO NOTHING no unique constraint yet  */
                    RETURNING id;
                    '''
            cursor = get_db_cursor()
            cursor.execute(query)
            result = cursor.fetchone()
            print(result)
            return result


def update_table(table, set_column, set_value, where_column, where_value):
    if table and set_column and set_value and where_column and where_value:
        log_update_same_table(table, set_column, where_column, where_value)
        query = f"UPDATE {table} SET {set_column} = '{sanitize(set_value)}' WHERE {where_column}='{sanitize(where_value)}'"
        execute(query)
