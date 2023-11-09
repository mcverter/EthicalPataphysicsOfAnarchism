import logging


class DBLogger:
    @staticmethod
    def log_update_same_table(set_column, where_column, counter):
        message = f'COMMITTING {set_column} for {where_column}. Counter is {counter}'
        logging.info(message)
        print(message)
