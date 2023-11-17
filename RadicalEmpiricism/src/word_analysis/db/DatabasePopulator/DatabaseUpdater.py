from .DBLogger import DBLogger
from .DatabasePopulator import DatabasePopulator
from ..db import select_from_table, update_table
import re

logger = DBLogger()



def get_where_value_from_row(cols):
    if re.search('^\(,', cols) or re.search(',\)$', cols):
        return None
    where_val = re.sub('.*,', '', cols)
    where_val = where_val[:-1]
    if where_val == "":
        return None
    return where_val


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
        raise Exception('Must define "get_data_value" in subclass')

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

            if counter == 41:
                print('break')
            where_value = get_where_value_from_row(row)
            if where_value:
                set_value = self.get_data_value(where_value)
                if set_value:
                    update_table(table=self.table,
                                        set_column=self.set_column,
                                        set_value=set_value,
                                        where_column=self.where_column,
                                        where_value=where_value)

            if counter % 50 == 3:
                self.commit(counter)
            counter += 1
        self.commit(counter)
