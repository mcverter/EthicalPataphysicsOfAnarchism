import functools

import requests
from bs4 import BeautifulSoup

from constants import TABLE_WORD, COLUMN_DEFINITION, COLUMN_ENGLISH, \
    SITE_ENGLISH_DEFINITIONS, COLUMN_ENGLISH_EXPLANATION
from z_radical_empiricism_logic.db.database_populator.foreign_key_updater import ForeignKeyUpdater
# TODO: this should be an arg to the constructor
OFFSET: int = 0


def find_english_definition(english):
    url = SITE_ENGLISH_DEFINITIONS + english
    page = requests.get(url, timeout=60)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find_all('div', {"class": "sense-content"})

    definition = functools.reduce(lambda a, b:
                                  a +
                                  b.text
                                  .replace('\n', '')
                                  .replace(':', '') +
                                  ";",
                                  results, '')
    if definition and len(definition) > 0:
        definition = definition[:-1] + '.'
    return definition


class EnglishDefinitionUpdater(ForeignKeyUpdater):
    def __init__(self):
        super().__init__(table=TABLE_WORD,
                         set_column=COLUMN_DEFINITION,
                         where_column=COLUMN_ENGLISH,
                         fk_internal_column=COLUMN_ENGLISH_EXPLANATION,
                         offset=OFFSET)

    def get_fk_value_from_main_where_value(self, where_value):
        return find_english_definition(where_value)


if __name__ == '__main__':
    updater = EnglishDefinitionUpdater()
    updater.populate()
