import logging

from deep_translator import GoogleTranslator
from RadicalEmpiricism.src.word_analysis.db.db import select_fields_from_word_table, update_word_table, commit_all

def populate_english_translation():
    french_words = select_fields_from_word_table(['french'])
    idx_global = 0
    for idx in range(len(french_words)):
        idx_global = idx
        french = french_words[idx][0]
        if french and idx > 15000:
            english = (GoogleTranslator(source='fr', target='en')).translate(french)
            if english:
                update_word_table('english', english, 'french', french)
                if idx % 100 == 25:
                    logging.info('COMMITTING english translation', idx)
                    commit_all()
    commit_all()
    logging.info('COMMITTING english translation done', idx_global)
