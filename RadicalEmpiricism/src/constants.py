import os

DB_LEVEL = "remote"

DB_ENGINE = "django.db.backends.postgresql"
DB_NAME = "word_analysis"
DB_PORT = "5432"

DB_LOCAL_USER = "postgres"
DB_LOCAL_PASS = os.environ["DB_PASS"]
DB_LOCAL_HOST = "localhost"
DB_REMOTE_USER = "mitchell.verter"
DB_REMOTE_PASS = os.environ["DB_REMOTE_PASS"]
DB_REMOTE_HOST = "ep-black-poetry-68818067.us-east-2.aws.neon.tech"
DB_RUNTIME_USER = DB_REMOTE_USER if DB_LEVEL == "remote" else DB_LOCAL_USER
DB_RUNTIME_PASSWORD = DB_REMOTE_PASS if DB_LEVEL == "remote" else DB_LOCAL_PASS
DB_RUNTIME_HOST = DB_REMOTE_HOST if DB_LEVEL == "remote" else DB_LOCAL_HOST

TABLE_WORD = DB_NAME + "_word"
TABLE_BOOK_LINE = DB_NAME + "_book_line"
OTB_FULL_FRENCH_TITLE = "Autrement qu'être ou Au-delà de l'essence"
TI_FULL_FRENCH_TITLE = "Totalité et infini : essai sur l'extériorité"
OTB_FULL_ENGLISH_TITLE = "Otherwise Than Being or Beyond Essence"
TI_FULL_ENGLISH_TITLE = 'Totality and Infinity: An Essay on Exteriority'
OTB_SHORT_FRENCH_TITLE = "Autrement"
TI_SHORT_FRENCH_TITLE = "Totalité"
OTB_SHORT_ENGLISH_TITLE = "Otherwise"
TI_SHORT_ENGLISH_TITLE = 'Totality'

COLUMN_FRENCH = "french"
COLUMN_FRENCH_EXPLANATION = "french_explanation"
COLUMN_ENGLISH = "english"
COLUMN_ENGLISH_EXPLANATION = "english_explanation"
COLUMN_ROOT = "root"
TI = "ti"
OTB = "otb"
COLUMN_DEFINITION = "definition"
COLUMN_SEMANTIC_CATEGORY = "semantic_category"
COLUMN_ETYMOLOGICAL_ROOT = "etymological_root"
COLUMN_ETYMOLOGY = "etymology"
COLUMN_VERB_TYPE = "verb_type"
COLUMN_NOUN_TYPE = "noun_type"
COLUMN_PART_OF_SPEECH = "part_of_speech"
COLUMN_SUFFIX = "suffix"
COLUMN_PREFIX = "prefix"

PATH_DIR = os.path.dirname(os.path.realpath(__file__))
LOG_DIR = os.path.join(PATH_DIR, '../src/z_radical_empiricism_logic/a_other/logs')
PATH_DB_POPULATE_LOG = os.path.join(LOG_DIR, "db_populate_log.txt")
PATH_DB_STATS_LOG = os.path.join(LOG_DIR, "db_stats_log.txt")

PATH_BOOKS = os.path.join(PATH_DIR, "books")
BOOK_AUTREMENT = os.path.join(PATH_BOOKS, "LevinasAutrementSpringer.txt")
BOOK_TOTALITE = os.path.join(PATH_BOOKS, "LevinasTotaLGF.txt")
CLEANED_SUFFIX = "cleaned.txt"
CLEANED_AUTREMENT = BOOK_AUTREMENT + CLEANED_SUFFIX
CLEANED_TOTALITE = BOOK_TOTALITE + CLEANED_SUFFIX

PATH_SENTENCES = os.path.join(PATH_BOOKS, "sentences")
OTB_FRENCH_SENTENCES = os.path.join(PATH_SENTENCES, 'otb_french_sentences.json')
TI_FRENCH_SENTENCES = os.path.join(PATH_SENTENCES, 'ti_french_sentences.json')
OTB_ENGLISH_SENTENCES = os.path.join(PATH_SENTENCES, 'otb_english_sentences.json')
TI_ENGLISH_SENTENCES = os.path.join(PATH_SENTENCES, 'ti_english_sentences.json')

SITE_FRENCH_DDF_ETYMOLOGY = "https://www.dictionnairedesfrancophones.org/form/"
SITE_FRENCH_DDF_TOKEN = "jss104"
SITE_ENGLISH_ETYMOLOGY = "https://www.etymonline.com/search?q="
SITE_ENGLISH_DEFINITIONS = "https://www.merriam-webster.com/dictionary/"
SITE_FRENCH_CNRTL_ETYMOLOGY = "https://www.cnrtl.fr/etymologie/"
SITE_FRENCH_CNRTL_TOKEN = "tlf_cvedette"
