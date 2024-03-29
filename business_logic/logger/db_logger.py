import logging
import os
from constants import PATH_DB_POPULATE_LOG

if not os.path.exists(PATH_DB_POPULATE_LOG):
    os.makedirs(os.path.dirname(PATH_DB_POPULATE_LOG), exist_ok=True)
    open(PATH_DB_POPULATE_LOG, "w+")

logging.basicConfig(filename=PATH_DB_POPULATE_LOG,
                    filemode='a',
                    format='%(asctime)s %(message)s',
                    level='DEBUG')


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
                        fk_internal_column,
                        where_value):
    message = f'UPDATE TABLE {table} ({set_column}) for FK{fk_internal_column}={where_value}.'
    log_and_print_message(message)


def log_update_fk_table_commit(table,
                               set_column,
                               fk_internal_column,
                               where_value,
                               counter):
    log_commit(counter)
    log_update_fk_table(table,
                        set_column,
                        fk_internal_column,
                        where_value)
