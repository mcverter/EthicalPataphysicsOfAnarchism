import logging

import requests
from bs4 import BeautifulSoup

from RadicalEmpiricism.src.word_analysis.db.db import update_table, select_from_table, commit_all
from RadicalEmpiricism.src.word_analysis.constants import SITE_ENGLISH_EXPLANATIONS, TABLE_WORD

OFFSET = 9220


def populate_english_explanation():
    english_words = select_from_table(TABLE_WORD, ("english",))

    idx_global = OFFSET

    for idx in range(len(english_words) - OFFSET):
        idx_global = OFFSET + idx
        english = english_words[idx][0]
        if english:
            english_url = english # JUST TEMP DEBUG f'{SITE_ENGlISH_EXPLANATIONS}{english}'
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
                update_table(TABLE_WORD, 'english_explanation', explanation, 'english', english)

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