from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('word_analysis', '0001_initial'),
    ]

    operations = [
        '''
        migrations.RunPython(addWordsToMap),
        migrations.RunPython(populate_english_translation),
        migrations.RunPython(populate_english_definition),
        migrations.RunPython(populate_english_etymology),
        migrations.RunPython(populate_french_definition),
        migrations.RunPython(populate_french_etymology),
    '''
    ]
