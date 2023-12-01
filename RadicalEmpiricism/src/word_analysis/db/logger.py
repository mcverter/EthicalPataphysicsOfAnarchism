import logging
from RadicalEmpiricism.src.constants import PATH_POPULATE_LOG

logging.basicConfig(filename=PATH_POPULATE_LOG,
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)


def log_and_print_message(message):
    logging.info(message)
    print(message)


def log_insert(table, columns):
    message = f'INSERT TABLE {table} COMMITTING {columns}.'
    log_and_print_message(message)


def log_commit(counter):
    message = f'COMMITTING ({counter})'
    log_and_print_message(message)


def log_insert_table_commit(table, columns, counter):
    log_commit(counter)
    log_insert(table, columns)


def log_update_same_table(table, set_column, where_column):
    message = f'UPDATE TABLE {table} COMMITTING {set_column} for {where_column}.'
    log_and_print_message(message)


def log_update_same_table_commit(table, set_column, where_column, counter):
    log_commit(counter)
    log_update_same_table(table, set_column, where_column)


def log_update_fk_table(table,
                        set_column,
                        where_column,
                        fk_table,
                        fk_internal_column):
    message = f'UPDATE TABLE {table} COMMITTING {set_column} for {where_column}. FK table {fk_table} COL {fk_internal_column}.'
    log_and_print_message(message)


def log_update_fk_table_commit(table,
                               set_column,
                               where_column,
                               fk_table,
                               fk_internal_column,
                               counter):
    log_commit(counter)
    log_update_fk_table(table,
                        set_column,
                        where_column,
                        fk_table,
                        fk_internal_column)
