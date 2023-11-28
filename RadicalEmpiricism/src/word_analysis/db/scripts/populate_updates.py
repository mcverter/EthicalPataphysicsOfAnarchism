from RadicalEmpiricism.src.word_analysis.db.database_populator.implementations.foreign_key_updaters.definition.english_definition_updater import \
    EnglishDefinitionUpdater
from RadicalEmpiricism.src.word_analysis.db.database_populator.implementations.foreign_key_updaters.definition.french_definition_updater import \
    FrenchDefinitionUpdater
from RadicalEmpiricism.src.word_analysis.db.database_populator.implementations.foreign_key_updaters.etymology.english_etymology_updater import \
    EnglishEtymologyUpdater
from RadicalEmpiricism.src.word_analysis.db.database_populator.implementations.foreign_key_updaters.etymology.french_etymology_updater import \
    FrenchEtymologyUpdater
from RadicalEmpiricism.src.word_analysis.db.database_populator.implementations.native_table_updaters.translation.english_translation_updater import \
    EnglishTranslationUpdater


def populate_definitions():
    updater = EnglishDefinitionUpdater()
    updater.populate()
    updater = FrenchDefinitionUpdater()
    updater.populate()


def populate_etymologies():
    updater = EnglishEtymologyUpdater()
    updater.populate()
    updater = FrenchEtymologyUpdater()
    updater.populate()


def populate_translations():
    updater = EnglishTranslationUpdater()
    updater.populate()


def populate_updates():
    populate_translations()
    populate_definitions()
    populate_etymologies()


if __name__ == '__main__':
    populate_updates()
