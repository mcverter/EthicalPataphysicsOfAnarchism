import re

from django import template
from django.urls import reverse

from constants import ABBREV_TO_FULL_TITLE_MAP
from word_analysis.hardcoded.accordion_data import accordion_route_to_title_data
from word_analysis.hardcoded.all_genres_data import genre_to_words, clean_genre_name
from word_analysis.hardcoded.constellation_example_data import (
    constellation_example_data,
)
from word_analysis.hardcoded.routes import (
    NAV_ITEMS,
)
from word_analysis.hardcoded.sentences.get_sentence import get_sentence

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
    return {"nav_items": NAV_ITEMS}


@register.inclusion_tag("nav/nav_bar.html")
def nav_bar(request):
    return {"request": request, "nav_items": NAV_ITEMS}


@register.inclusion_tag("tags/book_line_display.html")
def book_line_display(book, line_num, show_table_head=True):
    if str(line_num).find('_') == -1:
        line_start = line_end = line_num
    else:
        (line_start, line_end) = line_num.__str__.split('_')

    lines = [{"line_num": line_start + offset,
              "french_words": s["fr"].split(' '),
              "english_sentence": s["en"],
              }
             for offset, s in enumerate(
            get_sentence(book, num) for num in range(line_start, line_end + 1))]
    context = {
        "book": ABBREV_TO_FULL_TITLE_MAP[book],
        "lines": lines,
        "show_table_head": show_table_head
    }
    return context


@register.inclusion_tag("tags/constellation_example.html")
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
    return {"genre": clean_genre_name(genre), "words": genre_to_words(genre)}


@register.inclusion_tag("tags/bilingual_accordion.html")
def bilingual_accordion():
    return {}


@register.inclusion_tag("tags/inline_word_link.html")
def inline_word_link(word):
    return {"word": word}


@register.inclusion_tag("tags/content_card.html")
def content_card(section, expandable=True):
    return {
        "route": section["route"],
        "title": section["title"],
        "sub_sub_items": section.get("sub_sub_items"),
        "expandable": expandable
    }
