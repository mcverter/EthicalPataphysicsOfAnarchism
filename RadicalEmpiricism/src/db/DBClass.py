import psycopg2
from RadicalEmpiricism.src.logger import (
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

class DBHandler:
    def __init__(self):
        self.conn = psycopg2.connect(database=DB_NAME,
                            host=DB_RUNTIME_HOST,
                            user=DB_RUNTIME_USER,
                            password=DB_RUNTIME_PASSWORD,
                            port=DB_PORT)
    
    
    def get_db_cursor(self):
        return self.conn.cursor()
    
    
    def execute(self, query):
        cursor = self.get_db_cursor()
        cursor.execute(query)
    
    
    def execute_and_return_single_value(self, query):
        cursor = self.get_db_cursor()
        cursor.execute(query)
        results = cursor.fetchone()
        return results[0]
    
    
    def commit_all(self):
        self.conn.commit()
    
    
    def select_from_table(self, table, columns):
        if table and columns:
            cursor = self.get_db_cursor()
            query = f'SELECT ({",".join(columns)}) from {table}'
            cursor.execute(query)
            return cursor.fetchall()
        log_and_print_error("Table and Cols undefined: " + table + columns)
        return None
        
    def select_composite_id(self, table, columns, values):
        where_clause = f"WHERE {columns[0]}='{values[0]}' AND {columns[1]}={values[1]}"
        query = f"SELECT id from {table} {where_clause}"
        cursor = self.get_db_cursor()
        cursor.execute(query)
        result = cursor.fetchone()
        return None if result is None else result[0]
    
    
    def select_single_value(self, table, select_col, where_col, where_val):
        cursor = self.get_db_cursor()
        query = f"SELECT {select_col} from {table} where {where_col} = '{sanitize(where_val)}'"
        cursor.execute(query)
        result = cursor.fetchone()
        return None if result is None else result[0]
    
    
    def get_fk_value_from_main_main_table(self, main_table,
                                          main_set_column,
                                          main_where_column,
                                          main_where_val):
        return self.select_single_value(table=main_table,
                                   select_col=main_set_column,
                                   where_col=main_where_column,
                                   where_val=main_where_val)
    
    
    def update_foreign_key(self, main_table,
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
    
        log_update_fk_table(main_table, main_set_column, main_where_column, fk_table, fk_internal_column)
    
        fk_id = self.get_fk_value_from_main_main_table(main_table, main_set_column, main_where_column, main_where_val)
        if is_empty_value(fk_id):
            fk_id = self.insert_into_table(fk_table,
                                      columns=(fk_internal_column,),
                                      values=(data_value,))
            self.update_table(table=main_table,
                         set_column=main_set_column,
                         set_value=fk_id,
                         where_column=main_where_column,
                         where_value=main_where_val)
    
        else:
            # check table for value
            fk_internal_value = self.select_single_value(fk_table,
                                                    select_col=fk_internal_column,
                                                    where_col='id',
                                                    where_val=fk_id)
            if is_empty_value(fk_internal_value[0]):
                self.update_table(table=fk_table,
                             set_column=fk_internal_column,
                             set_value=data_value,
                             where_column='id',
                             where_value=fk_id)
    
    
    def no_unique_violation(self, table, columns, values):
        unique_column = columns[0]
        unique_value = values[0]
        single_result = self.select_single_value(table, unique_column, unique_column, unique_value)
        if is_empty_value(single_result):
            return True
        return False
    
    
    def insert_many_to_many(self, main_table, linked_table, columns, values):
        def composite_table():
            return main_table + linked_table[len('word_analysis'):]
    
        self.insert_into_table(composite_table(), columns, values)
    
    
    def insert_into_table(self, table, columns, values, unique=False):
        log_insert(table, columns, values)
    
        if is_empty_value(table) or is_empty_value(columns) or is_empty_value(values):
            log_and_print_error('insert_into_table undefined values: ' + table + columns + values)
            return None
    
        if not unique or self.no_unique_violation(table, columns, values):
            sanitized_values = [f'{v}' if isinstance(v, int) else f"'{sanitize(v)}'" for v in values]
            query = f'''
                    INSERT INTO {table} ({",".join(columns)}) 
                    VALUES ({",".join(sanitized_values)})
                    ON CONFLICT DO NOTHING
                    RETURNING id;
                    '''
            cursor = self.get_db_cursor()
            cursor.execute(query)
            result = cursor.fetchone()
            return None if result is None else result[0]
        else:
            return self.select_single_value(table, 'id', columns[0], values[0])
    
    
    def update_table(self, table, set_column, set_value, where_column, where_value):
        if table and set_column and set_value and where_column and where_value:
            log_update_same_table(table, set_column, where_column, where_value)
            query = f"UPDATE {table} SET {set_column} = '{sanitize(set_value)}' WHERE {where_column}='{sanitize(where_value)}'"
            self.execute(query)
