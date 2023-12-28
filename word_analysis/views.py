from django.shortcuts import render
from .word_counts import all_words_with_counts
from .models import Word
from constants import OTB, TI


def bootsy(request):
    return render(request, 'bootstrap_cards.html')


def words(request):
    context = {
        "words": all_words_with_counts,
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
        "book_lines": {
            "otb": otb_lines,
            "ti": ti_lines,
        },
        "etymology": etymology,
        "definition": definition
    }
    return render(request, 'pages/word_page.html', context)
