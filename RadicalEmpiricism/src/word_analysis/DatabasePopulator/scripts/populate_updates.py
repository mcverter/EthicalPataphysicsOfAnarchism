from ....DatabasePopulator.implementations.ForeignKeyUpdaters.Etymology.EnglishEtymologyUpdater import \
    EnglishEtymologyUpdater
from ....DatabasePopulator.implementations.ForeignKeyUpdaters.Etymology.FrenchEtymologyUpdater import \
    FrenchEtymologyUpdater
from ....DatabasePopulator.implementations.NativeTableUpdaters.Translation import \
    EnglishTranslationUpdater
from ....DatabasePopulator.implementations.ForeignKeyUpdaters.Definition.FrenchDefinitionUpdater import \
    FrenchDefinitionUpdater
from ....DatabasePopulator.implementations.ForeignKeyUpdaters.Definition.EnglishDefinitionUpdater import \
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
    populate_translations()
    populate_definitions()
    populate_etymologies()

if __name__ == '__main__':
    populate_updates()