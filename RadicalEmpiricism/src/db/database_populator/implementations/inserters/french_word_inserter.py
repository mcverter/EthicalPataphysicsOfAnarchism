import codecs
import json
import re

from RadicalEmpiricism.src.constants import TABLE_WORD, COLUMN_FRENCH, OTB_FRENCH_SENTENCES, TI_FRENCH_SENTENCES, \
    TI, OTB, TABLE_BOOK_LINE, TI_ENGLISH_SENTENCES, OTB_ENGLISH_SENTENCES
from RadicalEmpiricism.src.db.database_populator.database_inserter import DatabaseInserter
from RadicalEmpiricism.src.db.db import insert_into_table, select_single_value, select_composite_id, insert_many_to_many,\
    execute, commit_all
from RadicalEmpiricism.src.db.sanitize_values import sanitize
from RadicalEmpiricism.src.utils import is_empty_value

PUNCTUATION_MARKS = '[/.,()!?"]'

'''
THIS NEEDS TO BE ADDED BELOW
'''
def add_book_lines_text():
    for book in (TI, OTB):
        with codecs.open(get_french_filepath_from_book(book), 'r', 'utf-8-sig') as french_file:
            with codecs.open(get_english_filepath_from_book(book), 'r', 'utf-8-sig') as english_file:
                french_lines = json.load(french_file)
                english_lines = json.load(english_file)
                for idx in range(len(french_lines)):
                    query = f"""UPDATE {TABLE_BOOK_LINE} 
                                SET french='{sanitize(french_lines[idx])}',english='{sanitize(english_lines[idx])}'  
                                where book='{book}' and line={idx}"""
                    execute(query)
        commit_all()


def get_other_book(book):
    return OTB if book == TI else TI


def get_french_filepath_from_book(book):
    return TI_FRENCH_SENTENCES if book == TI else OTB_FRENCH_SENTENCES

def get_english_filepath_from_book(book):
    return TI_ENGLISH_SENTENCES if book == TI else OTB_ENGLISH_SENTENCES
    pass


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
                         columns=(COLUMN_FRENCH, TI, OTB))
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

    # need to add the lines too!
    def create_lines_table(self):
        for book in (TI, OTB):
            with codecs.open(get_french_filepath_from_book(book), 'r', 'utf-8-sig') as file:
                lines = json.load(file)
                for idx in range(len(lines)):
                    insert_into_table(TABLE_BOOK_LINE, ("book", "line"), (book, idx))
                    self.commit(666666)


def populate(self):
    self.create_lines_table()
    for book in (TI, OTB):
        with codecs.open(get_french_filepath_from_book(book), 'r', 'utf-8-sig') as file:
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
                  self.WORD_MAP[key][TI]['count'],
                  self.WORD_MAP[key][OTB]['count'])
        insert_into_table(TABLE_WORD, ("french", "ti", "otb"), values)

        if inner_counter % 50 == 6:
            self.commit(counter)
        inner_counter += 1
    self.commit(counter)

    for key in self.WORD_MAP.keys():
        for book in (TI, OTB):
            inner_counter = 0
            for line in self.WORD_MAP[key][book]["lines"]:
                word_id = select_single_value(TABLE_WORD, 'id', 'french', key)
                book_line_id = select_composite_id(TABLE_BOOK_LINE, ("book", "line"), (book, line))
                insert_many_to_many(TABLE_WORD, TABLE_BOOK_LINE, ('word_id', 'book_line_id'),
                                    (word_id, book_line_id))
                if inner_counter % 50 == 6:
                    self.commit(inner_counter)
                inner_counter += 1
    self.commit(counter)


if __name__ == '__main__':
    updater = FrenchWordInserter()
    updater.populate()
