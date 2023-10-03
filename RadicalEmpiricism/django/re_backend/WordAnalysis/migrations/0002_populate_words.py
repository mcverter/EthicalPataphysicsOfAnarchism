from django.db import migrations, transaction
from ..models import Word

WORD_MAP_PATH = '../../data/books/'
WORD_MAP_FILE = '{}WordMap.txt'.format(WORD_MAP_PATH)


def populate_my_table(apps, schema_editor):
    with transaction.atomic():
        with open(WORD_MAP_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                (french, ti, otb) = line.split(',')
                q = Word()
                q.french = french
                q.ti = ti
                q.otb = otb
                print("queue", q.french, q.ti, q.otb)
                q.save()

populate_my_table()
'''
class Migration(migrations.Migration):

    dependencies = [
        ('WordAnalysis', '0001_initial'),
    ]

    operations = [
      migrations.RunPython(populate_my_table),
    ]
'''