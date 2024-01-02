from django import template

register = template.Library()


@register.inclusion_tag('tags/fe_card.html')
def fe_card(value: str):
    return {"component_name": value}


@register.inclusion_tag('tags/french_english.html')
def fe_vertical(value: str):
    (french, english) = value.split("@")
    return {"french": french, "english": english}
