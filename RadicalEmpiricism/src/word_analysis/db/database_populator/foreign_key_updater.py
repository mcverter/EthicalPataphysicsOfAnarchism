from ..logger import log_update_fk_table_commit
from .database_updater import DatabaseUpdater
from RadicalEmpiricism.src.word_analysis.db.db import update_foreign_key
from RadicalEmpiricism.src.word_analysis.constants import TABLE_START_STRING



class ForeignKeyUpdater(DatabaseUpdater):
    def __init__(self,
                 table,
                 set_column,
                 where_column,
                 fk_internal_column,
                 offset):
        super().__init__(table=table,
                         set_column=set_column + '_id',
                         where_column=where_column,
                         offset=offset)
        self.fk_table = TABLE_START_STRING + set_column
        self.fk_internal_column = fk_internal_column

        self.offset = offset or 0

    def get_fk_value_from_main_where_value(self, where_value):
        raise Exception('Must define "get_fk_value_from_main_where_value" in subclass')

    def get_data_value(self, where_value):
        return update_foreign_key(main_table=self.table,
                                  main_set_column=self.set_column,
                                  main_where_column=self.where_column,
                                  main_where_val=where_value,
                                  fk_table=self.fk_table,
                                  fk_internal_column=self.fk_internal_column,
                                  data_value=self.get_fk_value_from_main_where_value(where_value))

    def commit(self, counter):
        super().commit(counter)
        log_update_fk_table_commit(self.table,
                                   self.set_column,
                                   self.where_column,
                                   self.fk_internal_column,
                                   counter)

