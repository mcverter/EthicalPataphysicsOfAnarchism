import os

TABLE_WORDS = 'word_analysis_word'
TABLE_DEFINITION = 'word_analysis_definition',
TABLE_SEMANTIC_CATEGORY = 'word_analysis_semanticcategory',
TABLE_ETYMOLOGICAL_ROOT = 'word_analysis_etymologicalroot',
TABLE_VERB_TYPE = 'word_analysis_verbtype',
TABLE_NOUN_TYPE = 'word_analysis_nountype',
TABLE_PART_OF_SPEECH = 'word_analysis_partofspeech',
TABLE_SUFFIX = 'word_analysis_suffix',
TABLE_PREFIX = 'word_analysis_prefix',
TABLE_WORD = 'word_analysis_word',

COLUMN_FRENCH = 'french'
COLUMN_FRENCH_EXPLANATION = 'french'
COLUMN_ENGLISH = 'french'
COLUMN_ENGLISH_EXPLANATION = 'french'
COLUMN_ROOT = 'root'


PATH_DIR = os.path.dirname(os.path.realpath(__file__))
PATH_BOOKS = os.path.join(PATH_DIR, 'data/books/')
PATH_WORD_MAP = os.path.join(PATH_DIR, '../../generated/word_map.csv')

BOOK_AUTREMENT = os.path.join(PATH_BOOKS,'AutrementABBYYOriginal.txt')
BOOK_TOTALITE = os.path.join(PATH_BOOKS,'TotaliteABBYYOriginal.txt')


SITE_FRENCH_ETYMOLOGY = 'https://www.dictionnairedesfrancophones.org/form/survivre'
SITE_ENGLISH_ETYMOLOGY = 'https://www.etymonline.com/search?q='
Site_ENGLISH_EXPLANATIONS = 'https://www.merriam-webster.com/dictionary/'

