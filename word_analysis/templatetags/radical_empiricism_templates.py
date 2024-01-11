from django import template

from constants import ABBREV_TO_FULL_TITLE_MAP
from word_analysis.hardcoded.all_genres_data import all_genres_to_words
from word_analysis.hardcoded.sentences.get_sentence import get_sentence

register = template.Library()


@register.inclusion_tag('tags/book_lines.html')
def book_line_display(book, line):
    return {
        "book": ABBREV_TO_FULL_TITLE_MAP[book],
        "lines": [{
            "num": line,
            "sentence": get_sentence(book, line)
        }]}


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
