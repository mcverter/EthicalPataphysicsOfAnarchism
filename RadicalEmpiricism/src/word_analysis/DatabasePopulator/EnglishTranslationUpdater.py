
from deep_translator import GoogleTranslator
from DatabaseUpdater import DatabaseUpdater

class EnglishTranslationUpdater(DatabaseUpdater):
    def __init__(self):
        super().__init__(table='', set_field='', where_field='', offset='')

    def get_set_value(self, where_value):
        return (GoogleTranslator(source='fr', target='en')).translate(where_value)
