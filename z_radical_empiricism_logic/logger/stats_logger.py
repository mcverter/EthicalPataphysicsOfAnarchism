import logging
from constants import PATH_DB_STATS_LOG

logging.basicConfig(filename=PATH_DB_STATS_LOG,
                    filemode='a',
                    format='%(asctime)s %(message)s',
                    level='DEBUG')


def log_stats_message(intro, sql_result):
    message = f'{intro}: {sql_result}'
    logging.info(message)
    print(message)
