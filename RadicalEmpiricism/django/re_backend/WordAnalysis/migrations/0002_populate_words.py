from django.db import migrations
from ..models import Word
WORD_MAP_PATH = '../../../../data/books/'
WORD_MAP_FILE = '{}WordMap.txt'.format(WORD_MAP_PATH)


def populate_my_table(apps, schema_editor):
    with (open(WORD_MAP_FILE, "r", encoding="utf-8") as f):
        lines = f.readlines()
        for line in lines:
            word = Word()
            (french, ti, otb) = line.split(',')
            word.french = french
            word.ti = ti
            word.otb = otb
            word.save()

class Migration(migrations.Migration):

    dependencies = [
        ('myapp', 'the_table_migration'),
    ]

    operations = [
      migrations.RunPython(populate_my_table),
    ]
