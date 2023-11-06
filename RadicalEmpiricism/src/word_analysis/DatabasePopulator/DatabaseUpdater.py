import logging
import re

from .DatabasePopulator import DatabasePopulator
from ..db.db import select_from_table, update_table, commit_all, insert_into_table

class DatabaseUpdater(DatabasePopulator):
    def __init__(self,
                 set_table,
                 where_table,
                 set_column,
                 where_column,
                 offset):
        self.set_table = set_table
        self.where_table = where_table
        self.set_column = set_column
        self.where_column = where_column

        self.OFFSET = offset or 0

    def get_set_value(self, where_value):
        raise Exception('Must define "get_set_value" in subclass')
        pass

    def do_commit(self, counter):
        message = f'COMMITTING {self.set_column} for {self.where_column}. Counter is {counter}'
        logging.info(message)
        print(message)
        commit_all()

    def where_value_is_empty(self, cols):
        return re.search('^\(,', cols) or re.search(',\)$', cols)

    def get_where_value(self, cols):
        return re.sub('[\(,\)]', '', cols)


    def update_foreign_key(self):

        # check foreign key table for id
        # if id does not exist, create it and return it
        # add foreign key id to main table
        pass
    def populate(self):
        rows = self.select_columns()

        counter = 0
        for row in rows:
            if row is None or counter < self.OFFSET:
                continue
            cols = row[0]
            if cols is None:
                continue
            if self.where_value_is_empty(cols):
                where_value = self.get_where_value(cols)
                set_value = self.get_set_value(where_value)
                self.update_single_item(set_value, where_value)
            if counter % 50 == 3:
                self.do_commit(counter)
            counter += 1
        self.do_commit(counter)

    def select_columns(self):
        return select_from_table(self.set_table, (self.set_column, self.where_column))

    def update_single_item(self, set_value, where_value):
        if self.where_table == self.set_table:
            return update_table(table=self.set_table,
                                set_column=self.set_column,
                                set_value=set_value,
                                where_column=self.where_column,
                                where_value=where_value)
        else:
            where_value_idx = select_from_table(self.where_table, (where_value))
            if where_value_idx:
                update_table(self.set_table, self.set_column, set_value, self.where_column, where_value_idx)
            else:
                idx = insert_into_table(self.where_table, self.where_column, where_value)
                update_table(self.set_table, self.set_column, set_value, self.where_column, idx)
