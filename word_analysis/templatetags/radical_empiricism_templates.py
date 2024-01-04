from django import template

from word_analysis.hardcoded.all_genres_data import all_genres_to_words

register = template.Library()


@register.inclusion_tag('tags/word_btn.html')
def word_btn(value: str):
    return {"word": value}


@register.inclusion_tag('tags/genre_btn_collapse.html')
def genre_btn_collapse(genre: str):
    return {"genre": genre, "words": all_genres_to_words(genre)}


@register.inclusion_tag('tags/bilingual_card.html')
def bilingual_card(value: str):
    return {"component_name": value}


@register.inclusion_tag('tags/bilingual_vertical.html')
def bilingual_vertical(value: str):
    (french, english) = value.split("@")
    return {"french": french, "english": english}
