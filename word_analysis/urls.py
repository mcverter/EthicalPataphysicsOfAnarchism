from django.urls import path
from .views import word_detail, words

urlpatterns = [
    path("", words, name="words"),
    path("words", words, name="words"),
    path("mots", words, name="words"),
    path("word/<str:word>/", word_detail, name="word"),
    path("mot/<str:word>/", word_detail, name="mot"),
]
