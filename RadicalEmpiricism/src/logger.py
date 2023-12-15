import logging
from RadicalEmpiricism.src.constants import PATH_DB_POPULATE_LOG

logging.basicConfig(filename=PATH_DB_POPULATE_LOG,
                    filemode='a',
                    format='%(asctime)s %(message)s',
                    level='INFO')


# '/home/mitchell/ComputerScience_Ubuntu/EthicalPataphysicsOfAnarchism/RadicalEmpiricism/src/logs/db_populate_log.txt'

def log_and_print_error(error):
    error_message = "ERROR ERROR " + error
    logging.error(error_message)
    print(error_message)


def log_and_print_message(message):
    logging.info(message)
    print(message)


def log_commit(counter):
    message = f'COMMITTING ({counter})'
    log_and_print_message(message)


def log_insert(table, columns, values):
    message = f'INSERT TABLE {table} COLS {columns} VALS {values}.'
    log_and_print_message(message)


def log_insert_table_commit(table, columns, values, counter):
    log_commit(counter)
    log_insert(table, columns, values)


def log_update_same_table(table, set_column, where_column, where_value):
    message = f'UPDATE TABLE {table} COMMITTING {set_column} for {where_column}={where_value}.'
    log_and_print_message(message)


def log_update_same_table_commit(table, set_column, where_column, where_value, counter):
    log_commit(counter)
    log_update_same_table(table, set_column, where_column, where_value)


"""
UPDATE TABLE word_analysis_word COMMITTING definition_id for english="". FK_INTERNAL_COL table word_analysis_definition COL english_explanation.
"""


def log_update_fk_table(table,
                        set_column,
                        where_column,
                        where_value,
                        fk_internal_column):
    message = f'UPDATE TABLE {table} COMMITTING {set_column} for {where_column}={where_value}. FK_COL {fk_internal_column}.'
    log_and_print_message(message)


def log_update_fk_table_commit(table,
                               set_column,
                               where_column,
                               where_value,
                               fk_internal_column,
                               counter):
    log_commit(counter)
    log_update_fk_table(table,
                        set_column,
                        where_column,
                        where_value,
                        fk_internal_column)
