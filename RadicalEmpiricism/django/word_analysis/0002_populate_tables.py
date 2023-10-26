from django.db import migrations
from RadicalEmpiricism.django.word_analysis.population_scripts.a_populate_words import populate_table_with_words
from RadicalEmpiricism.django.word_analysis.population_scripts.b_populate_english_translation import populate_english_translation
from RadicalEmpiricism.django.word_analysis.population_scripts.c_populate_french_definition import populate_french_definition
from RadicalEmpiricism.django.word_analysis.population_scripts.d_populate__english_definition import populate_english_definition
from RadicalEmpiricism.django.word_analysis.population_scripts.e_populate__english_etymology import populate_english_etymology
from RadicalEmpiricism.django.word_analysis.population_scripts.f_populate_french_etymology import populate_french_etymology

class Migration(migrations.Migration):

    dependencies = [
        ('word_analysis', '0001_initial'),
    ]

    operations = [
        '''
        migrations.RunPython(populate_table_with_words),
        migrations.RunPython(populate_english_translation),
        migrations.RunPython(populate_english_definition),
        migrations.RunPython(populate_english_etymology),
        migrations.RunPython(populate_french_definition),
        migrations.RunPython(populate_french_etymology),
    '''
    ]
