from RadicalEmpiricism.src.word_analysis.db.database_populator.implementations.foreign_key_updaters.definition.english_definition_updater import \
    EnglishDefinitionUpdater
from RadicalEmpiricism.src.word_analysis.db.database_populator.implementations.foreign_key_updaters.definition.french_definition_updater import \
    FrenchDefinitionUpdater

DO_FRENCH = False

def populate_definitions():
    if DO_FRENCH:
        updater = FrenchDefinitionUpdater()
        updater.populate()
    updater = EnglishDefinitionUpdater()
    updater.populate()

if __name__ == '__main__':
    populate_definitions()
