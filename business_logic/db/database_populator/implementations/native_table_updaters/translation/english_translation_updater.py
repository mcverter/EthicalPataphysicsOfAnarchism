from deep_translator import GoogleTranslator
from business_logic.db.database_populator.database_updater import DatabaseUpdater
from constants import TABLE_WORD, COLUMN_ENGLISH, COLUMN_FRENCH

OFFSET: int = 0


class EnglishTranslationUpdater(DatabaseUpdater):
    def __init__(self):
        super().__init__(table=TABLE_WORD,
                         set_column=COLUMN_ENGLISH,
                         where_column=COLUMN_FRENCH,
                         offset=OFFSET)

    def get_data_value(self, where_value):
        try:
            translation = (GoogleTranslator(source='fr', target='en')).translate(where_value)
            return translation
        except:
            return None


if __name__ == '__main__':
    updater = EnglishTranslationUpdater()
    updater.populate()
