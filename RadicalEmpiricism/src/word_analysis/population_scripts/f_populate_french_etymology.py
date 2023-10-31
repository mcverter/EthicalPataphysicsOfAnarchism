import logging

import requests
from bs4 import BeautifulSoup

from RadicalEmpiricism.src.word_analysis.db.db import update_word_table, select_fields_from_word_table, commit_all
from RadicalEmpiricism.src.word_analysis.constants import SITE_FRENCH_ETYMOLOGY

OFFSET = 0


def populate_french_etymology():
    french_words = select_fields_from_word_table(["french"])

    idx_global = 0

    for idx in range(len(french_words)):
        idx_global = idx
        french = french_words[idx][0]
        if french:
            french_url = f'{SITE_FRENCH_ETYMOLOGY}{french}'
            page = requests.get(french_url)
            soup = BeautifulSoup(page.content, "html.parser")
            results = soup.find_all('div', {"class": "sense-content"})

            etymology = ''
            for idx in range(len(results)):
                etymology = ((results[idx].text
                                .replace('\n', ''))
                               .replace(':', ''))
                etymology += etymology
                if idx < len(results):
                    etymology += "; "

            if etymology and idx >= OFFSET:
                update_word_table('french_etymology', etymology, 'french', french)

                logging.info(f'updating {french} with french_etymology')
                if idx % 100 == 29:
                    logging.info('COMMITTING french etymology', idx)
                    print('COMMITTING french etymology', idx)
                    commit_all()
    commit_all()
    logging.info('COMMITTING french etymology done', idx_global)


if __name__ == '__main__':
    populate_french_etymology()