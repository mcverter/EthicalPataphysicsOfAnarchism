
from deep_translator import GoogleTranslator
from DatabaseUpdater import DatabaseUpdater

class EnglishTranslationUpdater(DatabaseUpdater):
    def get_set_value(self, where_value):
        return (GoogleTranslator(source='fr', target='en')).translate(where_value)
