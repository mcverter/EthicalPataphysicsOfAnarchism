import psycopg2
from RadicalEmpiricism.src.z_radical_empiricism_logic.logger.db_logger import (
    log_insert,
    log_update_same_table,
    log_update_fk_table,
    log_and_print_error
)
from RadicalEmpiricism.src.constants import (
    DB_NAME,
    DB_PORT,
    DB_RUNTIME_USER,
    DB_RUNTIME_PASSWORD,
    DB_RUNTIME_HOST)
from RadicalEmpiricism.src.utils import is_empty_value
from .sanitize_values import sanitize

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


def execute_and_return_single_value(query):
    cursor = get_db_cursor()
    cursor.execute(query)
    results = cursor.fetchone()
    return results[0]


def commit_all():
    conn.commit()


def select_from_table(table, columns):
    if table and columns:
        cursor = get_db_cursor()
        query = f'SELECT ({",".join(columns)}) from {table}'
        cursor.execute(query)
        return cursor.fetchall()
    log_and_print_error("Table and Cols undefined: " + table + columns)
    return None


def select_composite_id(table, columns, values):
    where_clause = f"WHERE {columns[0]}='{values[0]}' AND {columns[1]}={values[1]}"
    query = f"SELECT id from {table} {where_clause}"
    cursor = get_db_cursor()
    cursor.execute(query)
    result = cursor.fetchone()
    return None if result is None else result[0]


def select_single_value(table, select_col, where_col, where_val):
    cursor = get_db_cursor()
    query = f"SELECT {select_col} from {table} where {where_col} = '{sanitize(where_val)}'"
    cursor.execute(query)
    result = cursor.fetchone()
    return None if result is None else result[0]


def get_fk_value_from_main_main_table(main_table,
                                      main_set_column,
                                      main_where_column,
                                      main_where_val):
    return select_single_value(table=main_table,
                               select_col=main_set_column,
                               where_col=main_where_column,
                               where_val=main_where_val)


def update_foreign_key(main_table,
                       main_set_column,
                       main_where_column,
                       main_where_val,
                       fk_table,
                       fk_internal_column,
                       data_value):
    if is_empty_value(main_where_val) or is_empty_value(main_where_column) \
            or is_empty_value(main_where_val) \
            or is_empty_value(fk_table) or is_empty_value(fk_internal_column) \
            or is_empty_value(main_set_column) or is_empty_value(data_value):
        log_and_print_error(f"""
        ERROR: you need to define all parameters to update_foreign_key
            main_table={main_table}
            main_set_column={main_set_column}
            main_where_column={main_where_column}
            main_where_val={main_where_val}
            fk_table={fk_table}
            fk_internal_column={fk_internal_column}
            data_value={data_value}
        """)

        return

    if main_where_val == 'pur':
        print('break')

    log_update_fk_table(main_table, main_set_column,  fk_internal_column, main_where_val)

    fk_id = get_fk_value_from_main_main_table(main_table, main_set_column, main_where_column, main_where_val)
    if is_empty_value(fk_id):
        fk_id = insert_into_table(fk_table,
                                  columns=(fk_internal_column,),
                                  values=(data_value,))
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
        if is_empty_value(fk_internal_value):
            update_table(table=fk_table,
                         set_column=fk_internal_column,
                         set_value=data_value,
                         where_column='id',
                         where_value=fk_id)


def no_unique_violation(table, columns, values):
    unique_column = columns[0]
    unique_value = values[0]
    single_result = select_single_value(table, unique_column, unique_column, unique_value)
    if is_empty_value(single_result):
        return True
    return False


def insert_many_to_many(main_table, linked_table, columns, values):
    def composite_table():
        return main_table + linked_table[len('word_analysis'):]

    insert_into_table(composite_table(), columns, values)


def insert_into_table(table, columns, values, unique=False):
    log_insert(table, columns, values)

    if is_empty_value(table) or is_empty_value(columns) or is_empty_value(values):
        log_and_print_error('insert_into_table undefined values: ' + table + columns + values)
        return None

    if not unique or no_unique_violation(table, columns, values):
        sanitized_values = [f'{v}' if isinstance(v, int) else f"'{sanitize(v)}'" for v in values]
        query = f'''
                INSERT INTO {table} ({",".join(columns)}) 
                VALUES ({",".join(sanitized_values)})
                ON CONFLICT DO NOTHING
                RETURNING id;
                '''
        cursor = get_db_cursor()
        cursor.execute(query)
        result = cursor.fetchone()
        return None if result is None else result[0]

    return select_single_value(table, 'id', columns[0], values[0])


def update_table(table, set_column, set_value, where_column, where_value):
    if table and set_column and set_value and where_column and where_value:
        log_update_same_table(table, set_column, where_column, where_value)
        query = f"UPDATE {table} SET {set_column} = '{sanitize(set_value)}' WHERE {where_column}='{sanitize(where_value)}'"
        execute(query)
