import logging
from RadicalEmpiricism.src.word_analysis.constants import PATH_POPULATE_LOG

logging.basicConfig(filename=PATH_POPULATE_LOG,
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)

def log_db_fk_update():
    message = f''
    logging.info(message)
    print(message)
def log_db_insert():
    message = f''
    logging.info(message)
    print(message)

def log_update_same_table(set_column, where_column, counter):
    message = f'COMMITTING {set_column} for {where_column}. Counter is {counter}'
    logging.info(message)
    print(message)
