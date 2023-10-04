# https://www.merriam-webster.com/dictionary/infinity
# https://www.larousse.fr/dictionnaires/francais/infini/42937
# >>> exec(open('myscript.py').read())
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
word_map_path = os.path.join(dir_path, '../../data/books/WordMap.txt')
from larousse_api import larousse

# Print the array containing all defintions of "Fromage"
print(larousse.get_definitions("Fromage"))