from RadicalEmpiricism.src.db.database_populator.implementations.foreign_key_updaters.definition.english_definition_updater import \
    EnglishDefinitionUpdater
from RadicalEmpiricism.src.db.database_populator.implementations.foreign_key_updaters.definition.french_definition_updater import \
    FrenchDefinitionUpdater
from RadicalEmpiricism.src.db.database_populator.implementations.foreign_key_updaters.etymology.english_etymology_updater import \
    EnglishEtymologyUpdater
from RadicalEmpiricism.src.db.database_populator.implementations.foreign_key_updaters.etymology.french_etymology_updater import \
    FrenchEtymologyUpdater


def populate_updates():
    FrenchEtymologyUpdater().populate()
    FrenchDefinitionUpdater().populate()
    # EnglishTranslationUpdater().populate()
    EnglishDefinitionUpdater().populate()
    EnglishEtymologyUpdater().populate()


if __name__ == '__main__':
    populate_updates()
