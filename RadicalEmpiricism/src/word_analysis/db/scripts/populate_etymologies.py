from RadicalEmpiricism.src.word_analysis.db.database_populator.implementations.foreign_key_updaters.etymology.english_etymology_updater import \
    EnglishEtymologyUpdater
from RadicalEmpiricism.src.word_analysis.db.database_populator.implementations.foreign_key_updaters.etymology.french_etymology_updater import \
    FrenchEtymologyUpdater

def populate_etymologies():
    updater = FrenchEtymologyUpdater()
    updater.populate()
    updater = EnglishEtymologyUpdater()
    updater.populate()

if __name__ == '__main__':
    populate_etymologies()
