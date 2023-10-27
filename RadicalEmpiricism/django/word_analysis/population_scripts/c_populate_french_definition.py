import re
import logging
from larousse_api import larousse
from RadicalEmpiricism.django.word_analysis.db.db import select_fields_from_word_table, update_word_table, commit_all


def clean_larousse_definition(definition):
    definition = definition.replace('\r\n', ' ')
    definition = definition.replace('\n', ' ')
    definition = definition.replace('\t', ' ')
    definition = definition.replace("'", "''")
    definition = re.sub('Synonymes.*', '', definition)

    return definition

def populate_french_expanation():
    french_words = select_fields_from_word_table(['french'])
    idx_global = 0
    for idx in range(len(french_words)):
        french = french_words[idx][0]
        if french and idx > 324:
            french_definition = larousse.get_definitions(french)
            if french_definition is not None and french_definition != []:
                all_definitions = []
                for definition in french_definition:
                    cleaned_definition = clean_larousse_definition(definition)
                    all_definitions.append(cleaned_definition)
                joined_definitions = ' '.join(all_definitions)
                update_word_table('french_explanation', joined_definitions, 'french', french)
                logging.info(f'updating {french} with french_explanation')
                if idx % 100 == 25:
                    logging.info('COMMITTING update', idx)
                    commit_all()
    commit_all()
    logging.info('COMMITTING done', idx_global)
