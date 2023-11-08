from ....DatabasePopulator.DatabaseInserter import DatabaseInserter
from ....constants import TABLE_WORD, COLUMN_FRENCH, COLUMN_TI, COLUMN_OTB


class FrenchWordInserter(DatabaseInserter):
    def __init__(self, values):
        work = TABLE_WORD
        print(work)
        super().__init__(table=TABLE_WORD,
                         columns=(COLUMN_FRENCH, COLUMN_TI, COLUMN_OTB),
                         values=values)

if __name__ == '__main__':
    values = []
    fwi = FrenchWordInserter(values)
