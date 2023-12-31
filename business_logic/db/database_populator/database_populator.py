from business_logic.logger.db_logger import log_commit

from ..db import commit_all


class DatabasePopulator:

    def __init__(self):
        print('creating instance of ' + self.__class__.__name__)

    def populate(self):
        raise Exception('populate must be defined by subclass')

    def commit(self, counter):
        log_commit(counter)
        commit_all()
