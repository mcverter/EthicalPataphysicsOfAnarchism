import logging

import requests
from bs4 import BeautifulSoup

from RadicalEmpiricism.src.word_analysis.db.db import update_word_table, select_fields_from_word_table, commit_all
from RadicalEmpiricism.src.word_analysis.constants import SITE_ENGLISH_EXPLANATIONS

OFFSET = 9220


def populate_english_explanation():
    english_words = select_fields_from_word_table(["english"])

    idx_global = OFFSET

    for idx in range(len(english_words) - OFFSET):
        idx_global = OFFSET + idx
        english = english_words[idx][0]
        if english:
            english_url = f'{SITE_ENGlISH_EXPLANATIONS}{english}'
            page = requests.get(english_url)
            soup = BeautifulSoup(page.content, "html.parser")
            results = soup.find_all('div', {"class": "sense-content"})

            explanation = ''
            for exidx in range(len(results)):
                explanation += ((results[exidx].text
                                .replace('\n', ''))
                               .replace(':', ''))
                if exidx < len(results):
                    explanation += "; "

            if explanation:
                update_word_table('english_explanation', explanation, 'english', english)

                logging.info(f'updating {english} with english_explanation')
                print(f'updating {english} with english_explanation', idx + OFFSET)
                if idx % 100 == 29:
                    logging.info('COMMITTING english explanation', idx + OFFSET)
                    print('COMMITTING english explanation', idx + OFFSET)
                    commit_all()
    commit_all()
    logging.info('COMMITTING english explanation done', idx_global)


if __name__ == '__main__':
    populate_english_explanation()