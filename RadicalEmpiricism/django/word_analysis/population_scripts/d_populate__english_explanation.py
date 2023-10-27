import logging

import requests
from bs4 import BeautifulSoup

from RadicalEmpiricism.django.word_analysis.db.db import update_word_table, select_fields_from_word_table, commit_all
from RadicalEmpiricism.django.word_analysis.constants import ENGlISH_EXPLANATIONS_SITE

OFFSET = 3620

def populate_english_explanation():
    english_words = select_fields_from_word_table(["english"])

    idx_global = 0
    
    for idx in range(len(english_words)):
        idx_global = idx
        english = english_words[idx][0]
        if english:
            english_url = f'{ENGlISH_EXPLANATIONS_SITE}{english}'
            page = requests.get(english_url)
            soup = BeautifulSoup(page.content, "html.parser")
            results = soup.find_all('div', {"class": "sense-content"})
            
            explanation = ''
            for idx in range(len(results)):
                explanation = ((results[idx].text
                              .replace('\n',''))
                              .replace(':', ''))
                explanation += explanation
                if idx < len(results):
                    explanation += "; "

            if explanation and idx > OFFSET:
                update_word_table('english_explanation', explanation, 'english', english)
                logging.info(f'updating {english} with english_explanation')
                if idx % 100 == 29:
                    logging.info('COMMITTING english explanation', idx)
                    print('COMMITTING english explanation', idx)
                    commit_all()
    commit_all()
    logging.info('COMMITTING english explanation done', idx_global)

    
if __name__ == '__main__':
    populate_english_explanation()