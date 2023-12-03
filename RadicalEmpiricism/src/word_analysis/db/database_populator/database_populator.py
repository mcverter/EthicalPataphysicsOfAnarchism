from RadicalEmpiricism.src.word_analysis.db.db import commit_all
from RadicalEmpiricism.src.logger import log_commit


class DatabasePopulator:

    def __init__(self):
        print('creating instance of ' + self.__class__.__name__)

    def populate(self):
        raise Exception('populate must be defined by subclass')

    def commit(self, counter):
        log_commit(counter)
        commit_all()
