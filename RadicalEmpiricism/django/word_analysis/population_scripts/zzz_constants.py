import os
WORDS_TABLE = 'WordAnalysis_word'

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
DB_FILE = os.path.join(DIR_PATH, '../../db.sqlite3')
ETYMONLINE_PATH = os.path.join(DIR_PATH, 'tests/html/etymonline.html')
FRENCH_ETYMOLOGY_PATH = os.path.join(DIR_PATH, 'tests/html/diccionairedesfrancophones.html')

FRENCH_ETYMOLOGY_SITE = 'https://www.dictionnairedesfrancophones.org/form/survivre'
ETYMONLINE_SITE ='https://www.etymonline.com/search?q=+relative'
ENGlISH_DEFINITIONS_SITE = 'https://www.merriam-webster.com/dictionary/'
BOOKS_PATH = 'RadicalEmpiricism/data/books/'
AUTREMENT = '{}AutrementABBYYOriginal.txt'.format(BOOKS_PATH)
TOTALITE = '{}TotaliteABBYYOriginal.txt'.format(BOOKS_PATH)
WORD_MAP = {}
# WORD_MAP_PATH = '{}WordMap.txt'.format(BOOKS_PATH)
dir_path = os.path.dirname(os.path.realpath(__file__))
WORD_MAP_PATH = os.path.join(dir_path, '../../generated/word_map.csv')
SQL_OUTPUT_FILE = os.path.join(dir_path, '../../generated/sql/french_definitions.sql')
sql_output_file = os.path.join(DIR_PATH, '../sql/english_definitions.sql')
