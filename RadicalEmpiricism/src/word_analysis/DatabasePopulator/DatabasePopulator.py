from ..db.db import commit_all


class DatabasePopulator:
    def commit(self, counter):
        commit_all()
