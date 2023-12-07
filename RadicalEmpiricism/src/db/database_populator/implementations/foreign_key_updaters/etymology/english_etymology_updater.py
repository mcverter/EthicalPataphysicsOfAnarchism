import re
import requests
from bs4 import BeautifulSoup

from RadicalEmpiricism.src.constants import (TABLE_WORD,
                                             COLUMN_ENGLISH,
                                             COLUMN_ETYMOLOGY,
                                             COLUMN_ENGLISH_EXPLANATION,
                                             SITE_ENGLISH_ETYMOLOGY)
from ....foreign_key_updater import ForeignKeyUpdater

OFFSET: int = 0


def is_etymology_div(div):
    attrs = div.attrs
    if 'class' in attrs:
        classes = attrs['class']
        for klass in classes:
            if re.match('^word__etymology_expand', klass):
                return True
    return False


class EnglishEtymologyUpdater(ForeignKeyUpdater):
    def __init__(self):
        super().__init__(table=TABLE_WORD,
                         set_column=COLUMN_ETYMOLOGY,
                         where_column=COLUMN_ENGLISH,
                         fk_internal_column=COLUMN_ENGLISH_EXPLANATION,
                         offset=OFFSET)

    def get_fk_value_from_main_where_value(self, where_value):
        if where_value:
            english_url = f'{SITE_ENGLISH_ETYMOLOGY}{where_value}'
            page = requests.get(english_url)
            soup = BeautifulSoup(page.content, "html.parser")
            results = soup.find_all('div')

            for result in results:
                if is_etymology_div(result):
                    return result.text
        else:
            print('break')


if __name__ == '__main__':
    updater = EnglishEtymologyUpdater()
    updater.populate()
