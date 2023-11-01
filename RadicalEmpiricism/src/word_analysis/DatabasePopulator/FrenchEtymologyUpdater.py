from DatabaseUpdater import DatabaseUpdater


class FrenchEtymologyUpdater(DatabaseUpdater):
    def __init__(self):
        super().__init__(table='', set_field='', where_field='', offset='')

    def get_set_value(self, where_value):
        pass

