from RadicalEmpiricism.src.word_analysis.db.database_populator.implementations.native_table_updaters.translation.english_translation_updater import \
    EnglishTranslationUpdater


def populate_translations():
    updater = EnglishTranslationUpdater()
    updater.populate()

if __name__ == '__main__':
    populate_translations()
