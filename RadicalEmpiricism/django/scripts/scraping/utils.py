import requests
import os
import re

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

dir_path = os.path.dirname(os.path.realpath(__file__))
etymonline_path = os.path.join(dir_path, './html/etymonline.html')

output = ''
english = 'foo'

with open(etymonline_path, "r", encoding="utf-8") as f:
    content = f.read()
    content = content.replace('\n', ' ')
    content = content.replace('\s+', ' ')
    etymology_re = '<div class="word__etymology_expand.*?data-more'
    etym_match = re.search(etymology_re, content)
    raw_div = etym_match.group(0)
    raw_div = re.sub('\s+', ' ', raw_div)
    raw_div = re.sub('<.*?>', '', raw_div)
    raw_div = re.sub('<a data-more', '', raw_div)
    raw_div = re.sub('^\s+', '', raw_div)
    output += f"UPDATE WordAnalysis_word SET english_etymology='{raw_div}' WHERE english='{english}';\n"
    print(raw_div)
