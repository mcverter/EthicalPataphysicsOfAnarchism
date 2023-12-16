from django.core.paginator import Paginator
from django.shortcuts import render

from ..models import Word


def listing(request):
    word_list = Word.objects.all()
    paginator = Paginator(word_list, 25)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "list.html", {"page_obj": page_obj})
