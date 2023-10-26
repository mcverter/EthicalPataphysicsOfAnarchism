from django.db import migrations
from a_populate_words import populate_table_with_words
from b_populate_english_translation import populate_english_translation
from c_populate_french_definition import populate_french_definition
from d_populate__english_definition import populate_english_definition
from e_populate__english_etymology import populate_english_etymology
from f_populate_french_etymology import populate_french_etymology

def populate_all():
     populate_table_with_words()
     '''
     populate_english_translation()
     populate_english_definition()
     populate_english_etymology()
     populate_french_definition()
     populate_french_etymology()
     '''
if __name__ == '__main__':
        populate_all()