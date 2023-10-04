import os
import csv
from RadicalEmpiricism.django.WordAnalysis.models import Word
dir_path = os.path.dirname(os.path.realpath(__file__))
word_map_path = os.path.join(dir_path, '../../data/books/WordMap.txt')


with open(word_map_path) as f:
    reader = csv.reader(f)
    for row in reader:
        _, created = Word.objects.get_or_create(
            french=row[0],
            ti=row[1],
            otb=row[2],
        )
        # creates a tuple of the new object or
        # current object and a boolean of if it was created