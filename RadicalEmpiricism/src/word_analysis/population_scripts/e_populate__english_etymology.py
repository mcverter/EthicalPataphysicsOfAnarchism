import logging
import re
import requests
from bs4 import BeautifulSoup

from ..db.db import update_table, select_from_table, commit_all
from ..constants import SITE_ENGLISH_ETYMOLOGY, TABLE_WORD

OFFSET = 0

# class="word__etymology_expand--1s7tE"
def is_etymology_div(div):
    attrs = div.attrs
    if 'class' in attrs:
        classes = attrs['class']
        for klass in classes:
            if re.match('^word__etymology_expand', klass):
                return True
    return False

def populate_english_etymology():
    english_words = select_from_table(TABLE_WORD, ("english",))

    idx_global = 0
    
    for idx in range(len(english_words)):
        idx_global = idx
        english = english_words[idx][0]
        if english:
            english_url = f'{SITE_ENGLISH_ETYMOLOGY}{english}'
            page = requests.get(english_url)
            soup = BeautifulSoup(page.content, "html.parser")
            results = soup.find_all('div')
            for result in results:
                if (is_etymology_div(result)):
                    print('MATCH', result)
                    etymology = result.text
                    if etymology and idx > OFFSET:
                        update_table(TABLE_WORD, 'english_etymology', etymology, 'english', english)
                        logging.info(f'updating {english} with english_etymology')
                        if idx % 100 == 29:
                            logging.info('COMMITTING english etymology', idx)
                            print('COMMITTING english etymology', idx)
                            commit_all()
                    break
    commit_all()
    logging.info('COMMITTING english explanation done', idx_global)

    
if __name__ == '__main__':
    populate_english_etymology()