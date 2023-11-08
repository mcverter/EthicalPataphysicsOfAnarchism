
from deep_translator import GoogleTranslator
from ....SameTableUpdater import SameTableUpdater
from ....constants import TABLE_WORD, COLUMN_ENGLISH, COLUMN_FRENCH

offset = 6300

class EnglishTranslationUpdater(SameTableUpdater):
    def __init__(self):
        super().__init__(set_table=TABLE_WORD,
                         where_table=TABLE_WORD,
                         set_column=COLUMN_ENGLISH,
                         where_column=COLUMN_FRENCH,
                         offset=offset)
    def get_set_value(self, where_value):
        return (GoogleTranslator(source='fr', target='en')).translate(where_value)
