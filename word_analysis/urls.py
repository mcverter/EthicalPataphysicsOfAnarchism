from django.urls import path, re_path
from .views import word_detail, words, bootsy

urlpatterns = [
    path("bootsy", bootsy, name="bootsy"),
    re_path(r"^$", words, name="words"),
    re_path(r"^words|mots$", words, name="words"),
    path("mot/<str:word>/", word_detail, name="word"),
    path("word/<str:word>/", word_detail, name="word"),


    # re_path(r"^articles/(?P<year>[0-9]{4})/$", views.year_archive),
    # cre_path("^word|mot/(?P<word>[.*])", word_detail, name="word"),
    # re_path(r"^confirm-email/(?P<key>[-:\w]+)/$", views.confirm_email, name="account_confirm_email"),

]
