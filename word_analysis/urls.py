from django.urls import re_path

from .views import debug_test, word_detail, word_list, translation_content_page, technical, summary, relations, \
    genre_list, genre_detail

urlpatterns = [
    re_path(r"^words|mots$", word_list, name="words"),
    re_path("^words|mots/(?P<prefix>.*)/$", word_list, name="words"),
    re_path("^word|mot/(?P<word>.*)/$", word_detail, name="word"),
    re_path(r"^genres|genres$", genre_list, name="genre_list"),
    re_path("^genre|genre/(?P<word>.*)/$", genre_detail, name="genre_detail"),

    re_path(r"^$", summary, name="summary"),
    re_path("^abstract$", translation_content_page, name="abstract"),
    re_path("^constellation$", translation_content_page, name="constellation"),
    re_path("^duality$", translation_content_page, name="duality"),
    re_path("^flat$", translation_content_page, name="flat"),
    re_path("^objective$", translation_content_page, name="objective"),
    re_path("^parallelism$", translation_content_page, name="parallelism"),
    re_path("^combination$", translation_content_page, name="combination"),
    re_path("^definition$", translation_content_page, name="definition"),
    re_path("^etymology$", translation_content_page, name="etymology"),
    re_path("^intersection$", translation_content_page, name="intersection"),
    re_path("^opposition$", translation_content_page, name="opposition"),
    re_path("^two_dimensional$", translation_content_page, name="two_dimensional"),
    re_path(r"^debug_test$", debug_test, name="debug_test"),

    # TODO: move these to BCP
    re_path(r"^relations$", relations, name="relations"),
    re_path(r"^summary|resume$", summary, name="summary"),
    re_path(r"^technical|technique$", technical, name="technical"),
]
