from multiprocessing import Process

from RadicalEmpiricism.src.db.database_populator.implementations.foreign_key_updaters.definition.english_definition_updater import \
    EnglishDefinitionUpdater
from RadicalEmpiricism.src.db.database_populator.implementations.foreign_key_updaters.definition.french_definition_updater import \
    FrenchDefinitionUpdater
from RadicalEmpiricism.src.db.database_populator.implementations.foreign_key_updaters.etymology.english_etymology_updater import \
    EnglishEtymologyUpdater
from RadicalEmpiricism.src.db.database_populator.implementations.foreign_key_updaters.etymology.french_etymology_updater import \
    FrenchEtymologyUpdater
from RadicalEmpiricism.src.db.database_populator.implementations.native_table_updaters.translation.english_translation_updater import \
    EnglishTranslationUpdater


def populate_english_updates():
    EnglishTranslationUpdater().populate()
    english_definition_updater = EnglishDefinitionUpdater()
    english_etymology_updater = EnglishEtymologyUpdater()
    p1 = Process(target=english_definition_updater.populate)
    p2 = Process(target=english_etymology_updater.populate)
    p1.start()
    p2.start()
    p1.join()
    p2.join()


def populate_french_updates():
    french_definition_updater = FrenchDefinitionUpdater()
    french_etymology_updater = FrenchEtymologyUpdater()
    p1 = Process(target=french_definition_updater.populate)
    p2 = Process(target=french_etymology_updater.populate)
    p1.start()
    p2.start()
    p1.join()
    p2.join()


def populate_updates():
    p1 = Process(target=populate_french_updates)
    p2 = Process(target=populate_english_updates)
    p1.start()
    p2.start()
    p1.join()
    p2.join()


def single_process_updates():
    FrenchEtymologyUpdater().populate()
    FrenchDefinitionUpdater().populate()
    EnglishTranslationUpdater().populate()
    EnglishDefinitionUpdater().populate()
    EnglishEtymologyUpdater().populate()


if __name__ == '__main__':
    # single_process_updates()
    populate_updates()

