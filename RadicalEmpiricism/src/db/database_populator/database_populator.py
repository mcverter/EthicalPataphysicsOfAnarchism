from RadicalEmpiricism.src.logger.db_logger import log_commit
from RadicalEmpiricism.src.db.DbHandler import DbHandler


class DatabasePopulator:

    def __init__(self):
        print('creating instance of ' + self.__class__.__name__)
        self.db_handler = DbHandler()

    def populate(self):
        raise Exception('populate must be defined by subclass')

    def commit(self, counter):
        log_commit(counter)
        self.db_handler.commit_all()
