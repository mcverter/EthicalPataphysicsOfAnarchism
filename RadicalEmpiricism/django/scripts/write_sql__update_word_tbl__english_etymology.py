import re
from utils import ETYMONLINE_PATH, update_word_table

def get_value_string_from_content(content, regex_start, regex_end):
    content = content.replace('\n', ' ')
    content = content.replace('\s+', ' ')
    full_regex = f'{regex_start}.*?{regex_end}'
    full_regex_search = re.search(full_regex, content)
    regex_match = full_regex_search.group(0)
    regex_match = re.sub(regex_start, '', regex_match)
    regex_match = re.sub(regex_end, '', regex_match)
    regex_match = re.sub('\s+', ' ', regex_match)
    regex_match = re.sub('^\s+', '', regex_match)
    regex_match = re.sub('<.*?>', '', regex_match)
    return regex_match

def add_english_etymology():
    output = ''
    english = 'foo'

    with open(ETYMONLINE_PATH, "r", encoding="utf-8") as f:
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
        return (raw_div)

    # output += update_word_table('english_definition', definition, 'english', word[0])


if __name__ == "__main__":
     add_english_etymology()