import re

PUNCTUATION_MARKS = '[/.,()!?"]'


def is_empty_value(value):
    if not value:
        return True
    return False


def remove_punctuation(line):
    return re.sub(PUNCTUATION_MARKS, '', line)


# is this redundant?
def remove_apostrophes(line):
    stems = ('l', 's', 'd', 'n', 'qu')
    for stem in stems:
        line = re.sub(f"{stem}['’]", f'{stem}e ', line)
    line = re.sub("['’]s", '', line)
    return line


def standardize_vowels(line):
    line = re.sub('[àâ]', 'a', line)
    line = re.sub('[éèêë]', 'e', line)
    line = re.sub('[îï]', 'i', line)
    line = re.sub('ô', 'o', line)
    line = re.sub('[ûüù]', 'u', line)
    line = re.sub('ç', 'c', line)
    return line
