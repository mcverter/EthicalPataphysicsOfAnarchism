from django import template

register = template.Library()

@register.inclusion_tag('tags/nav_item.html')
def nav_item(value: str):
    (french, english) = value.split(",")
    return {"french": french, "english": english}

@register.inclusion_tag('tags/word_list_header_item.html')
def word_list_header_item(value: str):
    (french, english) = value.split(",")
    return {"french": french, "english": english}
