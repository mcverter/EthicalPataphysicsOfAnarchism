from django import template

register = template.Library()


@register.inclusion_tag('tags/word_btn.html')
def word_btn(value: str):
    return {"word": value}


@register.inclusion_tag('tags/group_btn.html')
def group_btn(value: str):
    (count, name) = value.split("@")
    return {"name": name, "count": count}


@register.inclusion_tag('tags/fe_card.html')
def fe_card(value: str):
    return {"component_name": value}


@register.inclusion_tag('tags/french_english.html')
def fe_vertical(value: str):
    (french, english) = value.split("@")
    return {"french": french, "english": english}
