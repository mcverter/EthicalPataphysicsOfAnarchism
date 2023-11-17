from ..db import commit_all


class DatabasePopulator:

    def populate(self):
        raise Exception('populate must be defined by subclass')

    def commit(self, counter):
        commit_all()
