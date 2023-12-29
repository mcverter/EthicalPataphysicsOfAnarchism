from django import template

register = template.Library()

@register.inclusion_tag('tags/french_english.html')
def french_english(value: str):
    (french, english) = value.split("@")
    return {"french": french, "english": english}

@register.inclusion_tag('tags/french_english_span.html')
def french_english_span(value: str):
    (french, english) = value.split("@")
    return {"french": french, "english": english}
