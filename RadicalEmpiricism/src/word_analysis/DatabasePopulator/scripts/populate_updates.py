from RadicalEmpiricism.src.word_analysis.DatabasePopulator.implementations.Updaters.Etymology.EnglishEtymologyUpdater import \
    EnglishEtymologyUpdater
from RadicalEmpiricism.src.word_analysis.DatabasePopulator.implementations.Updaters.Etymology.FrenchEtymologyUpdater import \
    FrenchEtymologyUpdater
from RadicalEmpiricism.src.word_analysis.DatabasePopulator.implementations.Updaters.Translation.EnglishTranslationUpdater import \
    EnglishTranslationUpdater
from RadicalEmpiricism.src.word_analysis.DatabasePopulator.implementations.Updaters.Definition.FrenchDefinitionUpdater import \
    FrenchDefinitionUpdater
from RadicalEmpiricism.src.word_analysis.DatabasePopulator.implementations.Updaters.Definition.EnglishDefinitionUpdater import \
    EnglishDefinitionUpdater


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
#    populate_translations()
    populate_definitions()
    populate_etymologies()

if __name__ == '__main__':
    populate_updates()