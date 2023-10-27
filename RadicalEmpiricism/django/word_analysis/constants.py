import os
WORDS_TABLE = 'word_analysis_word'
DIR_PATH = os.path.dirname(os.path.realpath(__file__))

BOOKS_PATH = os.path.join(DIR_PATH, 'data/books/')
AUTREMENT = os.path.join(BOOKS_PATH,'AutrementABBYYOriginal.txt')
TOTALITE = os.path.join(BOOKS_PATH,'TotaliteABBYYOriginal.txt')

WORD_MAP_PATH = os.path.join(DIR_PATH, '../../generated/word_map.csv')


FRENCH_ETYMOLOGY_SITE = 'https://www.dictionnairedesfrancophones.org/form/survivre'
ENGLISH_ETYMOLOGY_SITE = 'https://www.etymonline.com/search?q='
ENGlISH_EXPLANATIONS_SITE = 'https://www.merriam-webster.com/dictionary/'

# FRENCH_ETYMOLOGY_PATH = os.path.join(DIR_PATH, 'tests/html/diccionairedesfrancophones.html')
