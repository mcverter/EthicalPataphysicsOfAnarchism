from deep_translator import GoogleTranslator

from RadicalEmpiricism.src.word_analysis.db.database_populator.database_updater import DatabaseUpdater
from RadicalEmpiricism.src.word_analysis.constants import TABLE_WORD, COLUMN_ENGLISH, COLUMN_FRENCH

OFFSET: int = 0


class EnglishTranslationUpdater(DatabaseUpdater):
    def __init__(self):
        super().__init__(table=TABLE_WORD,
                         set_column=COLUMN_ENGLISH,
                         where_column=COLUMN_FRENCH,
                         offset=OFFSET)

    def get_data_value(self, where_value):
        return (GoogleTranslator(source='fr', target='en')).translate(where_value)
