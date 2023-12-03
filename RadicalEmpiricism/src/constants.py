import os

DB_LEVEL = "local"

DB_ENGINE = "django.db.backends.postgresql"
DB_NAME = "word_analysis"
DB_PORT = "5432"

DB_LOCAL_USER = "postgres"
DB_LOCAL_PASS = os.environ["DB_PASS"]
DB_LOCAL_HOST = "localhost",
DB_REMOTE_USER = "mitchell.verter"
DB_REMOTE_PASS = os.environ["DB_REMOTE_PASS"]
DB_REMOTE_HOST = "ep-black-poetry-68818067.us-east-2.aws.neon.tech",
DB_RUNTIME_USER = DB_REMOTE_USER if DB_LEVEL == "remote" else DB_LOCAL_USER
DB_RUNTIME_PASSWORD = DB_REMOTE_PASS if DB_LEVEL == "remote" else DB_LOCAL_PASS
DB_RUNTIME_HOST = DB_REMOTE_HOST if DB_LEVEL == "remote" else DB_LOCAL_HOST


TABLE_WORD = DB_NAME + "_word"

COLUMN_FRENCH = "french"
COLUMN_FRENCH_EXPLANATION = "french_explanation"
COLUMN_ENGLISH = "english"
COLUMN_ENGLISH_EXPLANATION = "english_explanation"
COLUMN_ROOT = "root"
COLUMN_TI = "ti"
COLUMN_OTB = "otb"
COLUMN_DEFINITION = "definition"
COLUMN_SEMANTIC_CATEGORY = "semanticcategory"
COLUMN_ETYMOLOGICAL_ROOT = "etymologicalroot"
COLUMN_ETYMOLOGY = "etymology"
COLUMN_VERB_TYPE = "verbtype"
COLUMN_NOUN_TYPE = "nountype"
COLUMN_PART_OF_SPEECH = "partofspeech"
COLUMN_SUFFIX = "suffix"
COLUMN_PREFIX = "prefix"

PATH_DIR = os.path.dirname(os.path.realpath(__file__))
LOG_DIR = os.path.join(PATH_DIR, '../logs')
PATH_DB_POPULATE_LOG = os.path.join(LOG_DIR, "db_populate_log.txt")
PATH_BOOKS = os.path.join(PATH_DIR, "word_analysis/books")
PATH_WORD_MAP = os.path.join(PATH_DIR, "../../generated/word_map.csv")
BOOK_AUTREMENT = os.path.join(PATH_BOOKS, "LevinasAutrementSpringer.txt")
BOOK_TOTALITE = os.path.join(PATH_BOOKS, "LevinasTotaLGF.txt")
CLEANED_SUFFIX = "cleaned.txt"
CLEANED_AUTREMENT = BOOK_AUTREMENT + CLEANED_SUFFIX
CLEANED_TOTALITE = BOOK_TOTALITE + CLEANED_SUFFIX

SITE_FRENCH_DDF_ETYMOLOGY = "https://www.dictionnairedesfrancophones.org/form/"
SITE_FRENCH_DDF_TOKEN = "jss104"
SITE_ENGLISH_ETYMOLOGY = "https://www.etymonline.com/search?q="
SITE_ENGLISH_DEFINITIONS = "https://www.merriam-webster.com/dictionary/"
SITE_FRENCH_CNRTL_ETYMOLOGY = "https://www.cnrtl.fr/etymologie/"
SITE_FRENCH_CNRTL_TOKEN = "tlf_cvedette"
