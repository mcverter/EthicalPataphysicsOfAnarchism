from django.db import migrations
from ..models import Word
WORD_MAP_PATH = '../../../../data/books/'
WORD_MAP_FILE = '{}WordMap.txt'.format(WORD_MAP_PATH)


def populate_my_table(apps, schema_editor):
    with (open(WORD_MAP_FILE, "r", encoding="utf-8") as f):
        lines = f.readlines()
        for line in lines:
            (french, ti, otb) = line.split(',')
            w = Word(french=french, ti=ti, otb=otb)
            w.save()

class Migration(migrations.Migration):

    dependencies = [
        ('WordAnalysis', '0001_initial'),
    ]

    operations = [
      migrations.RunPython(populate_my_table),
    ]
