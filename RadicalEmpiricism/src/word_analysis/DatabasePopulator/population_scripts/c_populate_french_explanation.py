import re
import logging
from larousse_api import larousse
from RadicalEmpiricism.src.word_analysis.db.db import select_from_table, update_table, commit_all
from RadicalEmpiricism.src.word_analysis.constants import TABLE_WORD

OFFSET = 14700
def clean_larousse_definition(definition):
    definition = definition.replace('\r\n', ' ')
    definition = definition.replace('\n', ' ')
    definition = definition.replace('\t', ' ')
    definition = definition.replace("'", "''")
    definition = re.sub('Synonymes.*', '', definition)

    return definition

def populate_french_explanation():
    french_words = select_from_table(TABLE_WORD,('french',))
    idx_global = 0
    for idx in range(len(french_words)):
        french = french_words[idx][0]
        if french and idx > OFFSET:
            french_definition = larousse.get_definitions(french)
            if french_definition is not None and french_definition != []:
                all_definitions = []
                for definition in french_definition:
                    cleaned_definition = clean_larousse_definition(definition)
                    all_definitions.append(cleaned_definition)
                joined_definitions = ' '.join(all_definitions)
                update_table(TABLE_WORD, 'french_explanation', joined_definitions, 'french', french)
                logging.info(f'updating {french} with french_explanation')
                print(f'updating {french} with french_explanation')
                if idx % 100 == 29:
                    logging.info('COMMITTING french explanation', idx)
                    print('COMMITTING french explanation', idx)
                    commit_all()
    commit_all()
    logging.info('COMMITTING french explanation done', idx_global)
