from django import template

from constants import ABBREV_TO_FULL_TITLE_MAP
from word_analysis.hardcoded.all_genres_data import all_genres_to_words
from word_analysis.hardcoded.sentences.get_sentence import get_sentence
from word_analysis.hardcoded.constellation_example_data import constellation_example_data
from word_analysis.hardcoded.site_nav_data import nav_items

register = template.Library()


@register.inclusion_tag('tags/content_accordion.html')
def content_accordion(accordion):
    return {"accordion": accordion}


@register.inclusion_tag('nav/nav_bar.html')
def nav_bar():
    return {"nav_items": nav_items}


@register.inclusion_tag('nav/nav_bar_item.html')
def nav_bar_item(item, classes=""):
    return {"item": item, "classes": classes}


@register.inclusion_tag('nav/nav_bar_item_with_subitems.html')
def nav_bar_item_with_subitems(item):
    return {"item": item}


@register.inclusion_tag('tags/book_lines.html')
def book_line_display(book, line):
    return {
        "book": ABBREV_TO_FULL_TITLE_MAP[book],
        "lines": [{
            "num": line,
            "sentence": get_sentence(book, line)
        }]}


@register.inclusion_tag('tags/constellation_example.html')
def constellation_example():
    return {"constellation_example": constellation_example_data}


@register.inclusion_tag('tags/word_categorization_card.html')
def word_categorization_card(wc: str):
    return {"wc": wc}


@register.inclusion_tag('tags/word_btn.html')
def word_btn(value: str):
    return {"word": value}


@register.inclusion_tag('tags/genre_btn_collapse.html')
def genre_btn_collapse(genre: str):
    return {"genre": genre, "words": all_genres_to_words(genre)}


@register.inclusion_tag('tags/bilingual_card.html')
def bilingual_card(value: str):
    return {"component": value}


@register.inclusion_tag('tags/content_card.html')
def content_card(value: str):
    return {"component": value}


@register.inclusion_tag('tags/bilingual_vertical.html')
def bilingual_vertical(value: str):
    (french, english) = value.split("@")
    return {"french": french, "english": english}
