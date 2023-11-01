import re

def sanitize(value):
    if value.isnumeric():
        return value
    return re.sub("'", "''", value)

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
    regex_match = re.sub('^.*?>\s*', '', regex_match)
    regex_match = re.sub('<.*?$', '', regex_match)
    return regex_match
