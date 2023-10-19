from django.db import migrations
from ...population_scripts.a_populate_words import addWordsToMap
# from ...population_scripts.b_populate_english_translation import
from ...population_scripts.c_populate_french_definition import populate_french_definition
from ...population_scripts.d_populate__english_definition import  populate_english_definition
from ...population_scripts.e_populate__english_etymology import populate_english_etymology
# from ...population_scripts.f_populate_french_etymology import

class Migration(migrations.Migration):

    dependencies = [
        ('word_analysis', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(addWordsToMap),
        migrations.RunPython(populate_english_definition),
        migrations.RunPython(populate_english_etymology),
        migrations.RunPython(populate_french_definition()),
    ]

'''
def combine_names(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Person = apps.get_model("yourappname", "Person")
    for person in Person.objects.all():
        person.name = f"{person.first_name} {person.last_name}"
        person.save()


class Migration(migrations.Migration):
    dependencies = [
        ("yourappname", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(combine_names),
    ]
    '''