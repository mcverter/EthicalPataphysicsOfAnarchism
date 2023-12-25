from RadicalEmpiricism.src.z_radical_empiricism_logic.db.database_populator.implementations.inserters.french_word_inserter import \
    FrenchWordInserter


def populate_inserts():
    inserter = FrenchWordInserter()
    inserter.populate()


if __name__ == '__main__':
    populate_inserts()
