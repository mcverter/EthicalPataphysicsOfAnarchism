import re

from RadicalEmpiricism.src.constants import TABLE_WORD, COLUMN_FRENCH, COLUMN_TI, COLUMN_OTB, \
    CLEANED_AUTREMENT, CLEANED_TOTALITE
from ....database_populator.database_inserter import DatabaseInserter

WORD_MAP = {}


def split_into_words(content):
    content = content.replace('\n', ' ')
    content = content.replace('-', '')
    content = re.sub('[,.?()!]', ' ', content)
    content = re.sub(' +', ' ', content)
    words = content.split(' ')
    return words


def normalize_word(word):
    if len(word) == 0:
        return None
    word = re.sub('^\W+', '', word)
    word = word.replace('l\'', '')
    word = word.replace('d\'', '')
    return word.lower()


def add_words_to_map(words, book):
    for word in words:
        normalized = normalize_word(word)
        if normalized is None:
            pass
        elif normalized in WORD_MAP:
            WORD_MAP[normalized][book] += 1
        else:
            if book == 'ti':
                WORD_MAP[normalized] = {'ti': 1, 'otb': 0}
            else:
                WORD_MAP[normalized] = {'ti': 0, 'otb': 1}


class FrenchWordInserter(DatabaseInserter):
    def __init__(self):
        super().__init__(table=TABLE_WORD,
                         columns=(COLUMN_FRENCH, COLUMN_TI, COLUMN_OTB))
        self.WORD_MAP = {}

    def populate(self):
        with open(CLEANED_TOTALITE, "r", encoding="utf-8") as ti:
            ti_content = ti.read()
            ti_words = split_into_words(ti_content)
            add_words_to_map(ti_words, "ti")

        with open(CLEANED_AUTREMENT, "r", encoding="utf-8") as otb:
            otb_content = otb.read()
            otb_words = split_into_words(otb_content)
            add_words_to_map(otb_words, "otb")

        counter = 0
        for row in [
            (key[0], key[1]['ti'], key[1]['otb'])
            for key in WORD_MAP.items()]:
            if row[0] != 'parabreak':
                self.insert_single_item(row)
                counter += 1
                if counter % 50 == 14:
                    self.commit(counter)

        self.commit(counter)
