from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView
from django.views import View

from .models import Word, SemanticCategory, EtymologicalRoot, VerbType, NounType, Prefix, Suffix, PartOfSpeech


class AllPartOfSpeechView(ListView):
    template_name = ""
    model = PartOfSpeech
    ordering = ["-french"]
    context_object_name = "all_words"


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
    model = NounType
    ordering = ["-french"]
    context_object_name = "all_words"


class AllVerbTypeView(ListView):
    template_name = ""
    model = VerbType
    ordering = ["-french"]
    context_object_name = "all_words"


# Create your views here.
class AllEtymologicalRootView(ListView):
    template_name = ""
    model = EtymologicalRoot
    ordering = ["-french"]
    context_object_name = "all_words"


class AllSemanticCategoriesView(ListView):
    template_name = ""
    model = SemanticCategory
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


'''
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
        return render(request, "WordAnalysis/post-detail.html", context)

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
        return render(request, "WordAnalysis/post-detail.html", context)


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
