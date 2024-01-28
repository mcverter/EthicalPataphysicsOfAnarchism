from django import template
from utils import remove_punctuation, remove_apostrophes, standardize_vowels

register = template.Library()


@register.filter()
def normalize_french_word(word: str):
    return standardize_vowels(remove_punctuation(remove_apostrophes(remove_punctuation(word))))


@register.filter()
def starts_with(text: str, prefix: str):
    return text.startswith(prefix)


@register.filter()
def does_not_start_with(text: str, prefix: str):
    return text is not None and not text.startswith(prefix)


@register.filter()
def filter_by_letter(value_dict: dict, letter: str):
    if not letter:
        return value_dict
    return [v for v in value_dict if v.startswith(letter)]
