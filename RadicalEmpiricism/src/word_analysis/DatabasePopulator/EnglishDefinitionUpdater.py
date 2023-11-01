from DatabaseUpdater import DatabaseUpdater


class EnglishDefinitionUpdater(DatabaseUpdater):
    def __init__(self):
        super().__init__(table='', set_column='', where_column='', offset='')

    def get_set_value(self, where_value):
        pass

