import logging
import re
import requests
from bs4 import BeautifulSoup

from RadicalEmpiricism.django.word_analysis.db.db import update_word_table, select_fields_from_word_table, commit_all
from RadicalEmpiricism.django.word_analysis.constants import ENGLISH_ETYMOLOGY_SITE

OFFSET = 0

def is_definition_div(div):
    attrs = div.attrs
    if 'class' in attrs:
        classes = attrs['class']
        for klass in classes:
            if re.match('^word__defination', klass):
                return True
    return False

def populate_english_etymology():
    english_words = select_fields_from_word_table(["english"])

    idx_global = 0
    
    for idx in range(len(english_words)):
        idx_global = idx
        english = english_words[idx][0]
        if english:
            english_url = f'{ENGLISH_ETYMOLOGY_SITE}{english}'
            page = requests.get(english_url)
            soup = BeautifulSoup(page.content, "html.parser")
            results = soup.find_all('div')
            for result in results:
                if (is_definition_div(result)):
                    print('MATCH', result)
                    soup = result
            '''
            etymology = ''
            for idx in range(len(results)):
                etymology = ((results[idx].text
                              .replace('\n',''))
                              .replace(':', ''))
                etymology += etymology
                if idx < len(results):
                    etymology += "; "

            if etymology and idx > OFFSET:
                update_word_table('english_etymology', etymology, 'english', english)
                logging.info(f'updating {english} with english_etymology')
                if idx % 100 == 29:
                    logging.info('COMMITTING english etymology', idx)
                    print('COMMITTING english etymology', idx)
                    commit_all()
    commit_all()
    logging.info('COMMITTING english etymology done', idx_global)
    '''

    
if __name__ == '__main__':
    populate_english_etymology()