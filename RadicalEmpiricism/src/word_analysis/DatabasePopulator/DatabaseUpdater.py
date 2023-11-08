from DBLogger import Logger
from .DatabasePopulator import DatabasePopulator
from ..db.db import select_from_table, update_table
import re

logger = Logger()


def is_where_val_in_row(cols):
    return re.search('^\(,', cols) or re.search(',\)$', cols)


def get_where_value_from_row(cols):
    return re.sub('[(,)]', '', cols)


class DatabaseUpdater(DatabasePopulator):
    def __init__(self,
                 table,
                 set_column,
                 where_column,
                 offset):
        self.table = table
        self.set_column = set_column
        self.where_column = where_column
        self.offset = offset or 0

    def commit(self, counter):
        super().commit(counter)
        logger.log_update_same_table(self.set_column, self.where_column, counter)

    def get_data_value(self, where_value):
        raise Exception('Must define "crawl_web_for_where_value" in subclass')
        pass

    def select_columns(self):
        return select_from_table(self.table, (self.set_column, self.where_column))

    def populate(self):
        rows = self.select_columns()

        counter = 0
        for row in rows:
            if row is None or counter < self.offset:
                continue
            row = row[0]
            if row is None:
                continue
            if is_where_val_in_row(row):
                where_value = get_where_value_from_row(row)
                set_value = self.get_data_value(where_value)
                return update_table(table=self.table,
                                    set_column=self.set_column,
                                    set_value=set_value,
                                    where_column=self.where_column,
                                    where_value=where_value)

            if counter % 50 == 3:
                self.commit(counter)
            counter += 1
        self.commit(counter)
