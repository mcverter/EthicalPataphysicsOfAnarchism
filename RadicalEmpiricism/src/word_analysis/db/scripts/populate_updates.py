from RadicalEmpiricism.src.word_analysis.db.DatabasePopulator.Implementations.ForeignKeyUpdaters.Definition.EnglishDefinitionUpdater import \
    EnglishDefinitionUpdater
from RadicalEmpiricism.src.word_analysis.db.DatabasePopulator.Implementations.ForeignKeyUpdaters.Definition.FrenchDefinitionUpdater import \
    FrenchDefinitionUpdater
from RadicalEmpiricism.src.word_analysis.db.DatabasePopulator.Implementations.ForeignKeyUpdaters.Etymology.EnglishEtymologyUpdater import \
    EnglishEtymologyUpdater
from RadicalEmpiricism.src.word_analysis.db.DatabasePopulator.Implementations.ForeignKeyUpdaters.Etymology.FrenchEtymologyUpdater import \
    FrenchEtymologyUpdater
from RadicalEmpiricism.src.word_analysis.db.DatabasePopulator.Implementations.NativeTableUpdaters.Translation.EnglishTranslationUpdater import \
    EnglishTranslationUpdater


def populate_definitions():
    updater = FrenchDefinitionUpdater()
    updater.populate()
    updater = EnglishDefinitionUpdater()
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
    #    populate_translations()
    populate_definitions()


#    populate_etymologies()

if __name__ == '__main__':
    populate_updates()
