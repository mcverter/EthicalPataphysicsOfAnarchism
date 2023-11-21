from RadicalEmpiricism.src.word_analysis.db.db import insert_into_table
from .DatabasePopulator import DatabasePopulator


class DatabaseInserter(DatabasePopulator):
    def __init__(self,
                 table,
                 columns):
        self.table = table
        self.columns = columns

    def populate(self):
        raise Exception('populate must be defined by subclass')

    def insert_single_item(self, values):
        return insert_into_table(self.table, self.columns, values)
