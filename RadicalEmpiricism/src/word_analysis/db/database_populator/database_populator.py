from RadicalEmpiricism.src.word_analysis.db.db import commit_all


class DatabasePopulator:

    def __init__(self):
        print('creating instance of ' + self.__class__.__name__)

    def populate(self):
        raise Exception('populate must be defined by subclass')

    def commit(self, counter):
        commit_all()
