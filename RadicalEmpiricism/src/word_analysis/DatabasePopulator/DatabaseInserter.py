from ..db.db import insert_into_table
from DatabasePopulator import DatabasePopulator

class DatabaseInserter(DatabasePopulator):
    def __init__(self,
                 table,
                 columns,
                 values):
        self.table = table
        self.columns = columns
        self.values = values

    def insert(self):
        return insert_into_table(self.table, self.columns, self.values)
