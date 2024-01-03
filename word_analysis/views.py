from django.shortcuts import render

from constants import OTB, TI
from .hardcoded.all_genres_data import all_genres_to_words
from .hardcoded.all_words_data import all_words, proportion_ti_to_otb
from .models import Word


def genre_detail(request, genre):
    return render(request, 'pages/genre_list_page.html', {
        "genres": all_genres_to_words,
        "genre": genre
    })


def genre_list(request):
    return render(request, 'pages/genre_list_page.html', {
        "genres": all_genres_to_words,
    })


def word_list(request):
    context = {
        "words": all_words,
    }
    return render(request, 'pages/word_list_page.html', context)


def word_detail(request, word):
    book_word = Word.objects.get(french=word)
    if book_word is None:
        book_word = Word.objects.get(english=word)
    if book_word is None:
        return "could not find that word"
    etymology = book_word.etymology
    definition = book_word.definition
    otb_lines = book_word.book_line.all().order_by('line').filter(book=OTB)
    ti_lines = book_word.book_line.all().order_by('line').filter(book=TI)
    context = {
        "word": book_word,
        "sum": book_word.ti + book_word.otb,
        "proportion": proportion_ti_to_otb(book_word.ti, book_word.otb),
        "book_lines": {
            "otb": otb_lines,
            "ti": ti_lines,
        },
        "etymology": etymology,
        "definition": definition
    }
    return render(request, 'pages/word_detail_page.html', context)


def bilingual_content_page(request):
    return render(request, 'pages/bilingual_content_page.html')


# for on-the-fly UI testing
def debug_test(request):
    return render(request, 'pages/debug_test.html')


# refactor these all to bilingualW
def membership(request):
    return render(request, 'pages/membership_page.html')


def relations(request):
    return render(request, 'pages/relations_page.html')


def summary(request):
    return render(request, 'pages/summary_page.html')


def technical(request):
    return render(request, 'pages/technical_page.html')
