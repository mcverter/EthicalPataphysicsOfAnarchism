import re

from RadicalEmpiricism.src.constants import CLEANED_SUFFIX, BOOK_AUTREMENT, BOOK_TOTALITE


def fix_quotation_marks(text):
    return text


def fix_lapostrophe(text):
    text = re.sub(" Vess", " l'ess", text)
    text = re.sub(" Vau", " l'au", text)
    text = re.sub(" Y e", " l'e", text)
    text = re.sub(" Ye", " l'e", text)
    text = re.sub(" Yi", " l'i", text)
    return text


def remove_carat(text):
    return text


def remove_page_breaks(text):
    return text


class BookCleaner:
    def clean(self):
        text = self.material
        text = fix_quotation_marks(text)
        text = fix_lapostrophe(text)
        text = remove_carat(text)
        text = remove_page_breaks(text)
        return text

    def __init__(self, material):
        self.material = material


if __name__ == '__main__':
    paths = (BOOK_AUTREMENT, BOOK_TOTALITE)
    for path in paths:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
            cleaner = BookCleaner(content)
            cleaned = cleaner.clean()
            with open(path + CLEANED_SUFFIX, "w", encoding="utf-8") as g:
                g.write(cleaned)

    '''
content = re.sub('Yo', 'l\'o', content)
content = re.sub('Yu', 'l\'u', content)
content = re.sub('Vau', 'l\'au', content)
content = re.sub('Ve', 'l\'e', content)
content = re.sub('Vi', 'l\'i', content)
content = re.sub('Vo', 'l\'o', content)
content = re.sub('Vu', 'l\'u', content)
'''
