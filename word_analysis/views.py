from django.shortcuts import render, redirect
from django.db import connection

from constants import OTB, TI
from .hardcoded.all_genres_data import all_genres_to_words, all_words_to_genres
from .hardcoded.all_references_books import ALL_REFERENCE_BOOKS
from .hardcoded.all_words_get import all_words_with_counts, proportion_ti_to_otb
from .hardcoded.site_nav_data import (
    get_subitems_for_route,
    get_page_title_for_route,
)
from .hardcoded.routes import BRAND_ROUTE
from .models import Word


# top level pages
def genre_theory(request):
    return render(
        request,
        "pages/composite_page.html",
        {
            "toc_sections": get_subitems_for_route("genre_theory"),
            "page_title": get_page_title_for_route("genre_theory"),
        },
    )


def topics(request):
    return render(
        request,
        "pages/composite_page.html",
        {
            "toc_sections": get_subitems_for_route("topics"),
            "page_title": get_page_title_for_route("topics"),
        },
    )


def summary(request):
    return render(
        request,
        "pages/composite_page.html",
        {
            "toc_sections": BRAND_ROUTE["subitems"],
            "page_title": BRAND_ROUTE["title"],
        },
    )


def technical(request):
    return render(request, "pages/technical_page.html", {"books": ALL_REFERENCE_BOOKS})


# list and detail views
def word_list(request):
    context = {
        "words": all_words_with_counts(),
    }
    return render(request, "pages/word_list_page.html", context)


def word_detail(request, word):
    # fetch lines locally rather than querying db.  need to improve code though
    def get_book_lines(book_word_id):
        FIRST_OTB_LINE = 5046

        with connection.cursor() as cursor:
            query = f'select book_line_id from word_analysis_word_book_line where word_id = {book_word_id}'
            cursor.execute(query)
            results = cursor.fetchall()
            print('results', results)
            return ([result[0] - 1 for result in results if result[0] < FIRST_OTB_LINE],
                    [result[0] - FIRST_OTB_LINE for result in results if result[0] >= FIRST_OTB_LINE])

    try:
        book_word = Word.objects.select_related("etymology", "definition").get(french=word)
        (ti_lines, otb_lines) = get_book_lines(book_word.id)
        genres = all_words_to_genres(book_word)

        context = {
            "word": book_word,
            "sum": book_word.ti + book_word.otb,
            "proportion": proportion_ti_to_otb(book_word.ti, book_word.otb),
            "book_lines": {
                "otb": otb_lines,
                "ti": ti_lines,
            },
            "genres": genres,
            "etymology": book_word.etymology,
            "definition": book_word.definition,
        }
        return render(request, "pages/word_detail_page.html", context)

    except Word.DoesNotExist as exception:
        print('word does not exist', exception)
        return redirect('/mots')
    except Exception as exception:
        print('general exception', exception)


def genre_detail(request, genre):
    return render(
        request,
        "pages/genre_list_page.html",
        {"genres": all_genres_to_words, "genre": genre},
    )


def genre_list(request):
    return render(
        request,
        "pages/genre_list_page.html",
        {
            "genres": all_genres_to_words(),
        },
    )


def word_list_by_prefix(request, prefix):
    context = {
        "words": all_words_with_counts(),
    }
    return render(request, "pages/word_list_page.html", context)


# to display templates/content as a separate page
def content_page(request, name):
    return render(request, "pages/content_page.html", {"content": name})


# for debugging UI
def debug_test(request):
    return render(request, "pages/debug_test.html")
