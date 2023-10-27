import requests
from bs4 import BeautifulSoup

from RadicalEmpiricism.django.word_analysis.db.db import update_word_table, select_fields_from_word_table
from RadicalEmpiricism.django.word_analysis.constants import ENGlISH_EXPLANATIONS_SITE

def populate_english_explanation():
    english_words = select_fields_from_word_table(["english"])
    
    for idx in range(len(english_words)):
        english = english_words[idx][0]
        if english:
            english_url = f'{ENGlISH_EXPLANATIONS_SITE}{english}'
            page = requests.get(english_url)
            soup = BeautifulSoup(page.content, "html.parser")
            results = soup.find_all('div', {"class": "sense-content"})
            
            explanations = ''
            for idx in range(len(results)):
                explanation = ((results[idx].text
                              .replace('\n',''))
                              .replace(':', ''))
                explanations += explanation
                if idx < len(results):
                    explanations += "; "

            if explanations and idx > 0:
                output = update_word_table('english_explanation', explanations, 'english', english)
    
    
if __name__ == '__main__':
    populate_english_explanation()