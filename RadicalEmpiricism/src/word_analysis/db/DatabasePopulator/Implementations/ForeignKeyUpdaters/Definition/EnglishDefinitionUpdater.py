import requests
from bs4 import BeautifulSoup
from ....ForeignKeyUpdater import ForeignKeyUpdater
from ......constants import TABLE_WORD, COLUMN_DEFINITION, COLUMN_ENGLISH, SITE_ENGLISH_DEFINITIONS, COLUMN_ENGLISH_EXPLANATION

OFFSET: int = 0


def find_english_definition(english):
    url = SITE_ENGLISH_DEFINITIONS + english
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find_all('div', {"class": "sense-content"})

    # TODO: rewrite as a reduce
    definition = ''
    for exidx in range(len(results)):
        definition += ((results[exidx].text
                        .replace('\n', ''))
                       .replace(':', ''))
        if exidx < len(results):
            definition += "; "
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
