from django.urls import path

from . import views

urlpatterns = [
    path("", views.StartingPageView.as_view(), name="starting-page"),

    path("words", views.AllWordsView.as_view(), name="all-words-view"),
    path("mots", views.ToutesMotsView.as_view(), name="toutes-mots-view"),

    '''
    path("posts/<slug:slug>", views.SinglePostView.as_view(),
         name="post-detail-page"),  # /posts/my-first-post

    path("read-later", views.ReadLaterView.as_view(), name="read-later")
'''
]
