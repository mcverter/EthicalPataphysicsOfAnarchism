from .database_populator import DatabasePopulator
from ..db import insert_into_table


class DatabaseInserter(DatabasePopulator):
    def __init__(self,
                 table,
                 columns):
        super().__init__()
        self.table = table
        self.columns = columns

    def populate(self):
        raise Exception('populate must be defined by subclass')

    def insert_single_item(self, values, unique=False):
        return insert_into_table(self.table, self.columns, values, unique)
