from RadicalEmpiricism.src.z_radical_empiricism_logic.db.database_populator.implementations.foreign_key_updaters.definition.english_definition_updater import \
    EnglishDefinitionUpdater
from RadicalEmpiricism.src.z_radical_empiricism_logic.db.database_populator.implementations.foreign_key_updaters.definition.french_definition_updater import \
    FrenchDefinitionUpdater
from RadicalEmpiricism.src.z_radical_empiricism_logic.db.database_populator.implementations.foreign_key_updaters.etymology.english_etymology_updater import \
    EnglishEtymologyUpdater
from RadicalEmpiricism.src.z_radical_empiricism_logic.db.database_populator.implementations.foreign_key_updaters.etymology.french_etymology_updater import \
    FrenchEtymologyUpdater
from RadicalEmpiricism.src.z_radical_empiricism_logic.db.database_populator.implementations.native_table_updaters.translation.english_translation_updater import \
    EnglishTranslationUpdater


def populate_updates():
    EnglishTranslationUpdater().populate()
    FrenchEtymologyUpdater().populate()
    EnglishEtymologyUpdater().populate()
    EnglishDefinitionUpdater().populate()
    FrenchDefinitionUpdater().populate()


if __name__ == '__main__':
    populate_updates()
