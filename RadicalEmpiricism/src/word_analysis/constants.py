import os

TABLE_START_STRING = 'word_analysis_'
TABLE_WORD = TABLE_START_STRING + 'word'

COLUMN_FRENCH = 'french'
COLUMN_FRENCH_EXPLANATION = 'french_explanation'
COLUMN_ENGLISH = 'english'
COLUMN_ENGLISH_EXPLANATION = 'english_explanation'
COLUMN_ROOT = 'root'
COLUMN_TI = 'ti'
COLUMN_OTB = 'otb'
COLUMN_DEFINITION = 'definition'
COLUMN_SEMANTIC_CATEGORY = 'semanticcategory'
COLUMN_ETYMOLOGICAL_ROOT = 'etymologicalroot'
COLUMN_ETYMOLOGY = 'etymology'
COLUMN_VERB_TYPE = 'verbtype'
COLUMN_NOUN_TYPE = 'nountype'
COLUMN_PART_OF_SPEECH = 'partofspeech'
COLUMN_SUFFIX = 'suffix'
COLUMN_PREFIX = 'prefix'

PATH_DIR = os.path.dirname(os.path.realpath(__file__))
PATH_BOOKS = os.path.join(PATH_DIR, 'books')
PATH_WORD_MAP = os.path.join(PATH_DIR, '../../generated/word_map.csv')
BOOK_AUTREMENT = os.path.join(PATH_BOOKS, 'LevinasAutrementSpringer.txt')
BOOK_TOTALITE = os.path.join(PATH_BOOKS, 'LevinasTotaLGF.txt')
CLEANED_SUFFIX = 'cleaned.txt'
CLEANED_AUTREMENT = BOOK_AUTREMENT + CLEANED_SUFFIX
CLEANED_TOTALITE = BOOK_TOTALITE + CLEANED_SUFFIX

SITE_FRENCH_DDF_ETYMOLOGY = 'https://www.dictionnairedesfrancophones.org/form/'
SITE_FRENCH_DDF_TOKEN = 'jss104'
SITE_ENGLISH_ETYMOLOGY = 'https://www.etymonline.com/search?q='
SITE_ENGLISH_DEFINITIONS = 'https://www.merriam-webster.com/dictionary/'
SITE_FRENCH_CNRTL_ETYMOLOGY = 'https://www.cnrtl.fr/etymologie/'
SITE_FRENCH_CNRTL_TOKEN = 'tlf_cvedette'
