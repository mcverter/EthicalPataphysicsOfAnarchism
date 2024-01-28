from django import template
from django.urls import reverse

from constants import ABBREV_TO_FULL_TITLE_MAP
from word_analysis.hardcoded.all_genres_data import all_genres_to_words
from word_analysis.hardcoded.sentences.get_sentence import get_sentence
from word_analysis.hardcoded.constellation_example_data import (
    constellation_example_data,
)
from word_analysis.hardcoded.site_nav_data import (
    nav_items,
    get_page_title_for_route,
)
from word_analysis.hardcoded.accordion_data import accordion_route_to_title_data

register = template.Library()


@register.simple_tag
def active_check(request, urls):
    if request.path in (reverse(url) for url in urls.split()):
        return "active"
    return ""


@register.inclusion_tag("tags/content_accordion.html")
def content_accordion(route):
    return {"route": route, "title": accordion_route_to_title_data[route]}


@register.inclusion_tag("nav/page_toc.html")
def page_toc(page_title, toc_sections):
    return {"page_title": page_title, "toc_sections": toc_sections}


@register.inclusion_tag("nav/site_map_accordion.html")
def site_map_accordion():
    return {"nav_items": nav_items}


@register.inclusion_tag("nav/nav_bar.html")
def nav_bar(request):
    return {"request": request, "nav_items": nav_items}


@register.inclusion_tag("tags/book_line_display.html")
def book_line_display(book, line_num, show_table_head=True):
    sentence = get_sentence(book, line_num)
    # might need a better way to separate words
    french_words = sentence["fr"].split(' ')
    english_sentence = sentence["en"]
    context = {
        "book": ABBREV_TO_FULL_TITLE_MAP[book],
        "lines": [{"line_num": line_num,
                   "french_words": french_words,
                   "english_sentence": english_sentence,
                   }],
        "show_table_head": show_table_head
    }
    return context


@register.inclusion_tag("[]tags/constellation_example.html")
def constellation_example():
    return {"constellation_example": constellation_example_data}


@register.inclusion_tag("tags/word_categorization_card.html")
def word_categorization_card(wc: str):
    return {"wc": wc}


@register.inclusion_tag("tags/word_btn.html")
def word_btn(value: str):
    return {"word": value}


@register.inclusion_tag("tags/genre_btn_collapse.html")
def genre_btn_collapse(genre: str):
    return {"genre": genre, "words": all_genres_to_words(genre)}


@register.inclusion_tag("tags/bilingual_accordion.html")
def bilingual_accordion(value: str):
    return {"component": value}


@register.inclusion_tag("tags/content_card.html")
def content_card(route: str):
    return {"route": route, "title": get_page_title_for_route(route)}
