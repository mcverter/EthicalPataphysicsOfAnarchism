from ..db.db import select_from_table, update_query, execute
class DatabasePopulator:
    def __init__(self,  table, set_field, set_value, where_field, where_value):
        self.table = table
        self.set_field = set_field
        self.set_value = set_value

        self.where_field = where_field
        self.where_value = where_value
        pass

    def select_fields(self):
        return select_from_table(self.table, (self.set_field, self.where_field))

    def update_table(self):
        return update_query(table=self.table,
                            set_field=self.set_field,
                            set_value=self.set_value,
                            where_field=self.where_field,
                            where_value=self.where_value)

    def update_if_null(self):
        (set_val, where_val) = self.select_fields()


        if where_val is None:
            self.update_table()

    def run_update(self):


        pass
