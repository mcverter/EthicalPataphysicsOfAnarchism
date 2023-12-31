from django.shortcuts import render
from .word_quantities import all_word_quantities, proportion_ti_to_otb
from .models import Word
from constants import OTB, TI

def relations(request):
    return render(request, 'pages/relations_page.html')

def summary(request):
    return render(request, 'pages/summary_page.html')

def groups(request):
    return render(request, 'pages/groups_page.html')

def technical(request):
    return render(request, 'pages/technical_page.html')

def words(request):
    context = {
        "words": all_word_quantities,
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
    return render(request, 'pages/word_page.html', context)
