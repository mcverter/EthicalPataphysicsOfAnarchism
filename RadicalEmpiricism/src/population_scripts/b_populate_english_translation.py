import logging

from deep_translator import GoogleTranslator
from RadicalEmpiricism.src.word_analysis.db.db import select_from_table, update_table, commit_all
from RadicalEmpiricism.src.word_analysis.constants import TABLE_WORD

def populate_english_translation():
    french_words = select_from_table(TABLE_WORD, ('french',))
    idx_global = 0
    for idx in range(len(french_words)):
        idx_global = idx
        french = french_words[idx][0]
        if french and idx > 15000:
            english = (GoogleTranslator(source='fr', target='en')).translate(french)
            if english:
                update_table(TABLE_WORD, 'english', english, 'french', french)
                if idx % 100 == 25:
                    logging.info('COMMITTING english translation', idx)
                    commit_all()
    commit_all()
    logging.info('COMMITTING english translation done', idx_global)
