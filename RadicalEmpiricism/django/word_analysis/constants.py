import os
WORDS_TABLE = 'word_analysis_word'

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
DB_FILE = os.path.join(DIR_PATH, '../db.sqlite3')
ETYMONLINE_PATH = os.path.join(DIR_PATH, 'tests/html/etymonline.html')
FRENCH_ETYMOLOGY_PATH = os.path.join(DIR_PATH, 'tests/html/diccionairedesfrancophones.html')
WORD_MAP_PATH = os.path.join(DIR_PATH, '../../generated/word_map.csv')
SQL_OUTPUT_FILE = os.path.join(DIR_PATH, '../../generated/sql/french_definitions.sql')
sql_output_file = os.path.join(DIR_PATH, '../sql/english_definitions.sql')

FRENCH_ETYMOLOGY_SITE = 'https://www.dictionnairedesfrancophones.org/form/survivre'
ETYMONLINE_SITE ='https://www.etymonline.com/search?q=+relative'
ENGlISH_DEFINITIONS_SITE = 'https://www.merriam-webster.com/dictionary/'
BOOKS_PATH = os.path.join(DIR_PATH, 'data/books/')
AUTREMENT = os.path.join(BOOKS_PATH,'AutrementABBYYOriginal.txt')
TOTALITE = '{}TotaliteABBYYOriginal.txt'.format(BOOKS_PATH)
WORD_MAP = {}

