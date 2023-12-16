import codecs
import json
import re

from RadicalEmpiricism.src.constants import TABLE_WORD, COLUMN_FRENCH, OTB_FRENCH_SENTENCES, TI_FRENCH_SENTENCES, \
    COLUMN_TI, COLUMN_OTB, TABLE_BOOK_LINE
from RadicalEmpiricism.src.db.database_populator.database_inserter import DatabaseInserter
from RadicalEmpiricism.src.db.db import insert_into_table, insert_many_to_many, \
    select_composite_id, commit_all, select_single_value
from RadicalEmpiricism.src.utils import is_empty_value

PUNCTUATION_MARKS = '[/.,()!?"]'


def get_other_book(book):
    return COLUMN_OTB if book == COLUMN_TI else COLUMN_TI


def get_filepath_from_book(book):
    return TI_FRENCH_SENTENCES if book == COLUMN_TI else OTB_FRENCH_SENTENCES


def remove_punctuation(line):
    return re.sub(PUNCTUATION_MARKS, '', line)


def remove_apostrophes(line):
    stems = ('l', 's', 'd', 'n', 'qu')
    for stem in stems:
        line = re.sub(f"{stem}['’]", f'{stem}e ', line)
    line = re.sub("['’]s", '', line)
    return line


def standardize_vowels(line):
    line = re.sub('[àâ]', 'a', line)
    line = re.sub('[éèêë]', 'e', line)
    line = re.sub('[îï]', 'i', line)
    line = re.sub('ô', 'o', line)
    line = re.sub('[ûüù]', 'u', line)
    line = re.sub('ç', 'c', line)
    return line


def clean_line(line):
    line = remove_punctuation(line)
    line = line.lower()
    line = standardize_vowels(line)
    line = remove_apostrophes(line)
    return line


class WordMapEntry:
    def __init__(self, word):
        self.word = word
        self.lines = {}


class FrenchWordInserter(DatabaseInserter):
    def __init__(self):
        super().__init__(table=TABLE_WORD,
                         columns=(COLUMN_FRENCH, COLUMN_TI, COLUMN_OTB))
        self.WORD_MAP = {}

    def add_word_to_map(self, word, book, line):

        if is_empty_value(word) or re.match('\w', word) is None:
            return
        if word in self.WORD_MAP:
            self.WORD_MAP[word][book]["count"] += 1
            self.WORD_MAP[word][book]["lines"].add(line)
        else:
            self.WORD_MAP[word] = {
                book: {'count': 1, 'lines': {line}},
                get_other_book(book): {"count": 0, "lines": set()}
            }

    def create_lines_table(self):
        for book in (COLUMN_TI, COLUMN_OTB):
            with codecs.open(get_filepath_from_book(book), 'r', 'utf-8-sig') as file:
                lines = json.load(file)
                for idx in range(len(lines)):
                    insert_into_table(TABLE_BOOK_LINE, ("book", "line"), (book, idx))
        commit_all()

    def populate(self):
        self.create_lines_table()
        for book in (COLUMN_TI, COLUMN_OTB):
            with codecs.open(get_filepath_from_book(book), 'r', 'utf-8-sig') as file:
                lines = json.load(file)
                line_number = 0
                for line in lines:
                    line = clean_line(line)
                    for word in line.split(' '):
                        self.add_word_to_map(word, book, line_number)
                    line_number += 1
        counter = 0

        for key in self.WORD_MAP.keys():
            inner_counter = 0
            values = (key,
                      self.WORD_MAP[key][COLUMN_TI]['count'],
                      self.WORD_MAP[key][COLUMN_OTB]['count'])

            if inner_counter % 50 == 6:
                self.commit(counter)
            inner_counter += 1
        self.commit(counter)

        for key in self.WORD_MAP.keys():
            for book in (COLUMN_TI, COLUMN_OTB):
                inner_counter = 0
                for line in self.WORD_MAP[key][book]["lines"]:
                    word_id = select_single_value(TABLE_WORD, 'id', 'french', key)
                    if word_id == 16:
                        # key "il"
                        print(key, self.WORD_MAP[key], self.WORD_MAP[key][book]["lines"])
                    book_line_id = select_composite_id(TABLE_BOOK_LINE, ("book", "line"), (book, line))
                    insert_many_to_many(TABLE_WORD, TABLE_BOOK_LINE, ('word_id', 'book_line_id'), (word_id, book_line_id))
                if inner_counter % 50 == 6:
                    self.commit(inner_counter)
                inner_counter += 1
            self.commit(counter)
        self.commit(counter)


'''


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
        for row in [(key[0], key[1]["ti"], key[1]["otb"]) for key in WORD_MAP.items()]:
            if row[0] != "parabreak":
                self.insert_single_item(row)
                counter += 1
                if counter % 50 == 14:
                    self.commit(counter)

        self.commit(counter)
'''

if __name__ == '__main__':
    updater = FrenchWordInserter()
    updater.populate()
