
from .DatabaseUpdater import DatabaseUpdater
from ..db.db import update_foreign_key

class ForeignKeyUpdater(DatabaseUpdater):
    def __init__(self,
                 table,
                 set_column,
                 where_column,
                 offset,

                 # Foreign Key
                 fk_table,
                 main_where_col):
        super().__init__(table=table,
                         set_column=set_column,
                         where_column=where_column,
                         offset=offset)
        self.fk_table = fk_table
        self.main_where_col = main_where_col

        self.offset = offset or 0

    def update_fk(self,  where_value):
        update_foreign_key(main_table=self.table,
                           fk_table=self.fk_table,
                           main_where_col=self.main_where_col,
                           main_set_val=self.crawl_web_for_where_value(where_value),
                           main_fk_col='',
                           fk_where_col='',
                           fk_where_value=where_value)

    def get_set_value_for_main_table(self, where_value):
        raise Exception('Must define "get_set_value" in subclass')


