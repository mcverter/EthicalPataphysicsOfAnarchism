from .DatabaseUpdater import DatabaseUpdater
from ..db.db import update_foreign_key


class ForeignKeyUpdater(DatabaseUpdater):
    def __init__(self,
                 table,
                 main_set_column,
                 main_where_column,
                 fk_table,
                 fk_internal_column,
                 offset):
        super().__init__(table=table,
                         set_column=set_column,
                         where_column=where_column,
                         offset=offset)
        self.fk_table = fk_table
        self.main_where_col = main_where_col

        self.offset = offset or 0

    def update_fk(self, where_value):
        update_foreign_key(main_table=self.table,
                           main_where_column=self.main_where_col,
                           main_where_val='',
                           fk_table=self.fk_table,
                           main_fk_col='',
                           fk_internal_col='',
                           data_value=self.get_data_value(where_value))
