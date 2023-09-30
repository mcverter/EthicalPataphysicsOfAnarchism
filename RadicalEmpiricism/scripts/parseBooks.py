import re

BOOKS_PATH= 'RadicalEmpiricism/data/books/'
AUTREMENT = '{}AutrementABBYYOriginal.txt'.format(BOOKS_PATH)
TOTALITE = '{}TotaliteABBYYOriginal.txt'.format(BOOKS_PATH)
WORD_MAP = {}
WORD_MAP_PATH = '{}WordMap.txt'.format(BOOKS_PATH)

def read_file(path, book):
    with (open(path, "r", encoding="utf-8") as f):
        content = f.read()
        # remove punctuation
        content = re.sub('[\.\?\(\)\!:;,«»·°■]', '', content)
        content = re.sub(' ', '\n', content)
        # remove digits
        content = re.sub('\d+', '', content)
        # remove extra whitespace
        content = re.sub(' +', ' ', content)
        # il y a
        content = re.sub('il\ny\na', 'il-y-a', content)
        # reflexive verbs
        content = re.sub('\nse\n', '\nse-', content)
        # word break
        content = re.sub('-\n ', '', content)
        content = re.sub('- \n', '', content)
        content = re.sub('-\n', '', content)

        # l' misrecognition
        content = re.sub('Ya', 'l\'a', content)
        content = re.sub('Ye', 'l\'e', content)
        content = re.sub('Yi', 'l\'i', content)
        content = re.sub('Yo', 'l\'o', content)
        content = re.sub('Yu', 'l\'u', content)
        content = re.sub('Va', 'l\'a', content)
        content = re.sub('Ve', 'l\'e', content)
        content = re.sub('Vi', 'l\'i', content)
        content = re.sub('Vo', 'l\'o', content)
        content = re.sub('Vu', 'l\'u', content)
        content = re.sub('l\' ' , 'l\'', content)

        # comme misrecognition
        content = re.sub('co\^me', 'comme', content)
        content = re.sub('com\^e', 'comme', content)
        # lowercase
        content = content.lower()

        # sort words
        sorted = content.split('\n')
        filter(lambda a: a.length > 0, sorted)
        sorted.sort()
        addWordsToMap(sorted, book)
        sorted = '\n'.join(sorted)
        sorted = re.sub('\n+', '\n', sorted)

        # write out parsed files
        parsedPath = re.sub('Original', 'Parsed', path)
        with open(parsedPath, "w", encoding="utf-8") as f:
            f.write(sorted)



def addWordsToMap(words, book):
    for word in words:
        if (word in WORD_MAP):
            WORD_MAP[word][book] += 1
        else:
            if (book == 'ti'):
                WORD_MAP[word] = {'ti': 1, 'otb': 0}
            else:
                WORD_MAP[word] = {'ti': 0, 'otb': 1}

def writeWordMap():
    output = ''
    for key, value in WORD_MAP.items():
        output += '{},{},{}\n'.format(key, value['ti'], value['otb'])
        pass
    with open(WORD_MAP_PATH, "w", encoding="utf-8") as f:
        f.write(output)

read_file(AUTREMENT, 'otb')
read_file(TOTALITE, 'ti')
writeWordMap()