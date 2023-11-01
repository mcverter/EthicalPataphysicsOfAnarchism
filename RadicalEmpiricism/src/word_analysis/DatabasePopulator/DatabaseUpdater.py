import logging
from ..db.db import select_from_table, update_table, commit_all

class DatabaseUpdater:
    def __init__(self,
                 table,
                 set_field,
                 where_field,
                 offset):
        self.table = table
        self.set_field = set_field
        self.where_field = where_field

        self.OFFSET = offset or 1

    def get_where_value(self):
        raise Exception('Must define "get_where_value" in subclass')
        pass

    def do_commit(self, counter):
        message = f'COMMITTING {self.set_field} for {self.where_field}. Counter is {counter}'
        logging.info(message)
        print(message)
        commit_all()

    def populate(self):
        results = self.select_fields()

        counter = 0
        for result in results:
            (set_value, where_value) = result
            if where_value is None and counter >= self.OFFSET:
                where_value = self.get_where_value()
                self.update_single_item(set_value, where_value)
            if counter % 50 == 3:
                self.do_commit(counter)
            counter += 1
        self.do_commit(counter)

    def select_fields(self):
        return select_from_table(self.table, (self.set_field, self.where_field))

    def update_single_item(self, set_value, where_value):
        return update_table(table=self.table,
                            set_field=self.set_field,
                            set_value=set_value,
                            where_field=self.where_field,
                            where_value=where_value)
