from django import template
from django.template.defaultfilters import stringfilter
from django.utils.html import conditional_escape, mark_safe

register = template.Library()

@register.filter()
def filter_by_letter(value_dict: dict, letter: str):
    if not letter:
        return value_dict
    return [v for v in value_dict if v.startswith(letter)]

@register.inclusion_tag('tags/french_english.html')
def french_english(value: str):
    (french, english) = value.split("@")
    return {"french": french, "english": english}

@register.inclusion_tag('tags/french_english_span.html')
def french_english_span(value: str):
    (french, english) = value.split("@")
    return {"french": french, "english": english}
