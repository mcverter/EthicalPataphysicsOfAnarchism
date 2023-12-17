import logging
from RadicalEmpiricism.src.constants import PATH_DB_STATS_LOG

# 'C:\\Users\\Admin\\ComputerScience_Yoga\\EthicalPataphysicsOfAnarchism\\RadicalEmpiricism\\src\\../logs\\db_stats_log.txt'
logging.basicConfig(filename=PATH_DB_STATS_LOG,
                    filemode='a',
                    format='%(asctime)s %(message)s',
                    level='DEBUG')


def log_stats_message(intro, sql_result):
    message = f'{intro}: {sql_result}'
    logging.info(message)
    print(message)
