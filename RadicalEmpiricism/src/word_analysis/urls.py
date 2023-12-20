from django.urls import path
from .views import mot_detail, Index

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("word/<str:word>/", mot_detail, name="word"),
    path("mot/<str:word>/", mot_detail, name="mot"),
]

'''
# ex: /polls/5/results/
path("<int:question_id>/results/", views.results, name="results"),
# ex: /polls/5/vote/
path("<int:question_id>/vote/", views.vote, name="vote"),
path("", views.StartingPageView.as_view(), name="starting-page"),
path("words", views.AllWordsView.as_view(), name="all-words-view"),
path("mots", views.ToutesMotsView.as_view(), name="toutes-mots-view"),

path("posts/<slug:slug>", views.SinglePostView.as_view(),
     name="post-detail-page"),  # /posts/my-first-post

path("read-later", views.ReadLaterView.as_view(), name="read-later")
'''
