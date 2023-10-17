import re
from utils import ETYMONLINE_PATH, update_word_table, get_value_string_from_content


def add_english_etymology():
    output = ''
    english = 'foo'

    with open(ETYMONLINE_PATH, "r", encoding="utf-8") as f:
        content = f.read()
        value = get_value_string_from_content(content, '<div class="word__etymology_expand', 'data-more')
        output = update_word_table('english_etymology', value, 'english', english)
        return output

if __name__ == "__main__":
     add_english_etymology()