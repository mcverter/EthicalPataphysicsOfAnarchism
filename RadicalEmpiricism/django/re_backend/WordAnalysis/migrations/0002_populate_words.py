WORD_MAP_PATH = '../../../../data/books/'
WORD_MAP_FILE = '{}WordMap.txt'.format(WORD_MAP_PATH)

with (open(WORD_MAP_FILE, "r", encoding="utf-8") as f):
    lines = f.readlines()
    for line in lines:
        (word, ti, otb) = line.split(',')
