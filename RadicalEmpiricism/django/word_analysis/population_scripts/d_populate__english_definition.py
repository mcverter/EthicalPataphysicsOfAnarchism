import os
import requests
from bs4 import BeautifulSoup

from RadicalEmpiricism.django.word_analysis.db.db import update_word_table
from RadicalEmpiricism.django.word_analysis.constants import DIR_PATH, ENGlISH_DEFINITIONS_SITE

def populate_english_definition():
    sql_output_file = os.path.join(DIR_PATH, '../sql/english_definitions.sql')


    # english_words = select_fields_from_word_table(["english"])
    english_words = ('infinity',)

    for word in english_words:
        english_url = f'{ENGlISH_DEFINITIONS_SITE}{word}'

        page = requests.get(english_url)

        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find_all('div', {"class": "sense-content"})
        all_text = ''
        for idx in range(len(results)):
            definition = ((results[idx].text
                          .replace('\n',''))
                          .replace(':', ''))
            print(definition)
            all_text += definition
            if idx < len(results):
                all_text += "; "
        print(all_text)

        definition = all_text

        output = update_word_table('english_definition', definition, 'english', word)

        with open(sql_output_file, "w", encoding="utf-8") as g:
            g.write(output)
            # write the sql

# https://www.merriam-webster.com/dictionary/infinity
# https://www.larousse.fr/dictionnaires/francais/infini/42937
# >>> exec(open('myscript.py').read())

if __name__ == '__main__':
    populate_english_definition()