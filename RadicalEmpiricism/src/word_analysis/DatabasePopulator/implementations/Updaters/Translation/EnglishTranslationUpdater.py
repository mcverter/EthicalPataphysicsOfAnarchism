
from deep_translator import GoogleTranslator
from ....DatabaseUpdater import DatabaseUpdater
from RadicalEmpiricism.src.word_analysis.constants import TABLE_WORD, COLUMN_ENGLISH, COLUMN_FRENCH

OFFSET = 0

class EnglishTranslationUpdater(DatabaseUpdater):
    def __init__(self):
        super().__init__(set_table=TABLE_WORD,
                         where_table=TABLE_WORD,
                         set_column=COLUMN_ENGLISH,
                         where_column=COLUMN_FRENCH,
                         offset=OFFSET)
    def get_set_value(self, where_value):
        return (GoogleTranslator(source='fr', target='en')).translate(where_value)
