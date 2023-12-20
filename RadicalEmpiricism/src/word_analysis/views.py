from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views.generic import TemplateView, ListView, DetailView, View
from django.views import View
from .models import Word, Semantic_Categories, Etymological_Root, Verb_Type, \
    Noun_Type, Prefix, Suffix, Part_Of_Speech
from RadicalEmpiricism.src.constants import OTB, TI


def word_detail(request, english):
    word = get_object_or_404(Word, english=english)
    book_lines = word.book_line.all().order_by('-book')
    print('book lines', book_lines)

    context = {
        "word": word,
        "book_lines": book_lines
    }
    return render(request, 're_templates/word.html', context)


def mot_detail(request, arg_word):
    book_word = Word.objects.get(french=arg_word)
    if book_word is None:
        book_word = Word.objects.get(english=arg_word)
    if book_word is None:
        return ("could not find that word")
    etymology = book_word.etymology
    definition = book_word.definition
    otb_lines = book_word.book_line.all().order_by('-line').filter(book=OTB)
    ti_lines = book_word.book_line.all().order_by('-line').filter(book=TI)

    context = {
        "word": word,
        "book_lines": {
            "otb": otb_lines,
            "ti": ti_lines,
        },
        "etymology": etymology,
        "definition": definition
    }
    return render(request, 're_templates/word.html', context)


class Index(ListView):
    model = Word
    template_name = 're_templates/index.html'


class MotDetailView(DetailView):
    template_name = 're_templates/word.html'

    # query_pk_and_slug = "french"

    def get_object(self, queryset=None):
        french = self.kwargs['french']
        return Word.objects.get(french=french)


class WordDetailView(DetailView):
    model = Word
    template_name = 're_templates/word.html'
    query_pk_and_slug = "english"


"""
he DetailView's get_object method already knows how to fetch an object by the slug. There's no need to duplicate this code, just call super().

Then you can compare the user to self.request.user directly - there's no need to refetch the user from the database with get_object_or_404.

Finally, you can't return a response from get_object, the method is meant to return the object. You can however raise an exception like Http404.

from django.http import Http404

class PhotoDetail(DetailView):

    def get_object(self, queryset=None):
        obj = super(PhotoDetail, self).get_object(queryset=queryset)
        if obj.user != obj.photoextended.user:
            raise Http404()
        return obj
A common approach in class based views is to override get_queryset and filter by user. The get_object method will use this queryset when fetching the object. If the object is not in the queryset, then the user will get a 404 error.

class PhotoDetail(DetailView):

    def get_queryset(self):
        queryset = super(PhotoDetail, self).get_queryset()
        return queryset.filter(photoextended__user=self.request.user)
Share
Follow
edited Mar 7, 2017 at 16:52
answered Mar 7, 2017 at 16:21
Alasdair's user avatar
Alasdair
302k5656 gold badges583583 silver badges520520 bronze badges
Thanks for the great answer seems to work perfectly. I change it to this as it wanted a queryset 'class PhotoDetail(DetailView): template_name = 'otologue/photo_detail.html' queryset = Photo.objects def get_queryset(self): queryset = super(PhotoDetail, self).get_queryset() return queryset.filter(photoextended__user=self.request.user)' – 
Alex Haines
 Mar 7, 2017 at 16:34 
It just seems confusing as to how it manages to get the correct Photo object. Does the queryset automatically look for the slug in the query results and compare it with the slugfield in the url – 
Alex Haines
 Mar 7, 2017 at 16:37
1
The get_object method starts with the queryset from get_queryset, and filters using the slug from the URL to get the object. You might find ccbv useful to explore how the methods in class based views fit together. – 
Alasdair
 Mar 7, 2017 at 16:49 
Add a comment
Your Answer
"""


def index(request):
    word_list = Word.objects.all().values()
    return HttpResponse("Hello, world. You're at the polls index.")


def word(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def listing(request):
    word_list = Word.objects.all()
    # paginator = Paginator(word_list, 25)  # Show 25 contacts per page.

    # page_number = request.GET.get("page")
    # page_obj = paginator.get_page(page_number)
    # return render(request, "list.html", {"page_obj": page_obj})
    return render('hello world')


class AllPartOfSpeechView(ListView):
    template_name = ""
    model = Part_Of_Speech
    ordering = ["-french"]
    context_object_name = "all_words"


'''

class AllPrefixView(ListView):
    template_name = ""
    model = Prefix
    ordering = ["-french"]
    context_object_name = "all_words"


class AllSuffixView(ListView):
    template_name = ""
    model = Suffix
    ordering = ["-french"]
    context_object_name = "all_words"


# Create your views here.
class AllNounTypeView(ListView):
    template_name = ""
    model = Noun_Type
    ordering = ["-french"]
    context_object_name = "all_words"


class AllVerbTypeView(ListView):
    template_name = ""
    model = Verb_Type
    ordering = ["-french"]
    context_object_name = "all_words"


# Create your views here.
class AllEtymologicalRootView(ListView):
    template_name = ""
    model = Etymological_Root
    ordering = ["-french"]
    context_object_name = "all_words"


class AllSemanticCategoriesView(ListView):
    template_name = ""
    model = Semantic_Categories
    ordering = ["-french"]
    context_object_name = "all_words"


class AllWordsView(ListView):
    template_name = ""
    model = Word
    ordering = ["-french"]
    context_object_name = "all_words"


class ToutesMotsView(ListView):
    template_name = ""
    model = Word
    ordering = ["-french"]
    context_object_name = "all_posts"


class AllWordsEnglishView(ListView):
    template_name = ""
    model = Word
    ordering = ["-english"]
    context_object_name = "all_posts"


class SinglePostView(View):
    def is_stored_post(self, request, post_id):
        stored_posts = request.session.get("stored_posts")
        if stored_posts is not None:
            is_saved_for_later = post_id in stored_posts
        else:
            is_saved_for_later = False

        return is_saved_for_later

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)

        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": CommentForm(),
            "comments": post.comments.all().order_by("-id"),
            "saved_for_later": self.is_stored_post(request, post.id)
        }
        return render(request, "word_analysis/post-detail.html", context)

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()

            return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))

        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": comment_form,
            "comments": post.comments.all().order_by("-id"),
            "saved_for_later": self.is_stored_post(request, post.id)
        }
        return render(request, "word_analysis/post-detail.html", context)


class StartingPageView(ListView):
    template_name = ""
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data
'''
