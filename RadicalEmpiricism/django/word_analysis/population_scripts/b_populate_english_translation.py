from deep_translator import GoogleTranslator
from RadicalEmpiricism.django.word_analysis.db.db import select_fields_from_word_table, update_word_table, commit_all

def populate_english_translation():
    french_words = select_fields_from_word_table(['french'])
    all_updates = ''
    idx_global = 0
    for idx in range(len(french_words)):
        idx_global = idx
        french = french_words[idx]
        if french[0] and idx > 12624:
            english = (GoogleTranslator(source='fr', target='en')).translate(french[0])
            if english:
                update_word_table('english', english, 'french', french[0])
                if idx % 100 == 25:
                    print('committing', idx)
                    commit_all()
    commit_all()
    print('done committing', idx_global)
