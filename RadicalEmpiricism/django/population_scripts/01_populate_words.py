import re
from .constants import WORD_MAP, WORD_MAP_PATH, AUTREMENT, TOTALITE

def process_book_file(path, book):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
        cleaned = cleanFileContent(content)
        cleaned = cleaned.split('\n')
        filter(lambda a: a.length > 0, cleaned)
        addWordsToMap(cleaned, book)
        sorted_and_cleaned = '\n'.join(cleaned)

        # write out parsed files
        processed_path = re.sub('Original', 'Parsed', path)
        with open(processed_path, "w", encoding="utf-8") as f:
            f.write(sorted_and_cleaned)
def cleanFileContent(content):
    content = re.sub('[\.\?\(\)\!"\t:;,«»·°”■’“•﻿]', '', content)
    content = re.sub(' ', '\n', content)
    # remove digits
    content = re.sub('\d+', '', content)
    # remove extra whitespace
    content = re.sub(' +', ' ', content)
    # il y a
    content = content.replace('Il\ny\na', 'il-y-a')
    content = content.replace('il\ny\na', 'il-y-a')

    # reflexive verbs
    content = re.sub('\nse\n', '\nse-', content)
    content = re.sub(' se ', ' se-', content)

    # word break
    content = re.sub(' +-', '-', content)
    content = re.sub('-\n ', '', content)
    content = re.sub('- \n', '', content)
    content = re.sub('-\n', '', content)
    content = re.sub('-\n', '', content)

    # l' misrecognition
    content = re.sub('Ya', 'l\'a', content)
    content = re.sub('Ye', 'l\'e', content)
    content = re.sub('Yi', 'l\'i', content)
    content = re.sub('Yo', 'l\'o', content)
    content = re.sub('Yu', 'l\'u', content)
    content = re.sub('Vau', 'l\'au', content)
    content = re.sub('Ve', 'l\'e', content)
    content = re.sub('Vi', 'l\'i', content)
    content = re.sub('Vo', 'l\'o', content)
    content = re.sub('Vu', 'l\'u', content)
    content = re.sub('l\' +', 'l\'', content)
    content = re.sub('d\' +', 'd\'', content)
    content = re.sub('d +\'', 'd\'', content)
    content = re.sub(' +\'', '', content)

    # comme misrecognition
    content = re.sub('co\^me', 'comme', content)
    content = re.sub('com\^e', 'comme', content)
    content = re.sub('\n+', '\n', content)
    return content

def writeWordMap():
    output = ''
    for key, value in WORD_MAP.items():
        output += '{},{},{}\n'.format(key, value['ti'], value['otb'])
        pass
    with open(WORD_MAP_PATH, "w", encoding="utf-8") as f:
        f.write(output)

def normalizeWord(word):
    if len(word) == 0:
        return None
    word = word.replace('l\'', '')
    word = word.replace('d\'', '')
    return word.lower()

def addWordsToMap(words, book):
    for word in words:
        normalized = normalizeWord(word)
        if (normalized is None):
            pass
        elif (normalized in WORD_MAP):
            WORD_MAP[normalized][book] += 1
        else:
            if (book == 'ti'):
                WORD_MAP[normalized] = {'ti': 1, 'otb': 0}
            else:
                WORD_MAP[normalized] = {'ti': 0, 'otb': 1}


process_book_file(AUTREMENT, 'otb')
process_book_file(TOTALITE, 'ti')
writeWordMap()
