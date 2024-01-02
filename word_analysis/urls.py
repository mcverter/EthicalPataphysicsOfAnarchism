from django.urls import re_path

from .views import debug_test, word_detail, words, bilingual_content_page, groups, technical, summary, relations, \
    membership

urlpatterns = [
    re_path(r"^$", summary, name="summary"),
    re_path(r"^debug_test$", debug_test, name="debug_test"),
    re_path("^abstract$", bilingual_content_page, name="abstract"),
    re_path("^constellation$", bilingual_content_page, name="constellation"),
    re_path("^doubling$", bilingual_content_page, name="doubling"),
    re_path("^flat$", bilingual_content_page, name="flat"),
    re_path("^objective$", bilingual_content_page, name="objective"),
    re_path("^parallelism$", bilingual_content_page, name="parallelism"),
    re_path("^combination$", bilingual_content_page, name="combination"),
    re_path("^definition$", bilingual_content_page, name="definition"),
    re_path("^etymology$", bilingual_content_page, name="etymology"),
    re_path("^intersection$", bilingual_content_page, name="intersection"),
    re_path("^opposition$", bilingual_content_page, name="opposition"),
    re_path("^two_dimensional$", bilingual_content_page, name="two_dimensional"),

    # TODO: move these to BCP
    re_path(r"^relations$", relations, name="relations"),
    re_path(r"^membership$", membership, name="membership"),
    re_path(r"^summary|resume$", summary, name="summary"),
    re_path(r"^groups|groupes$", groups, name="groups"),
    re_path(r"^technical|technique$", technical, name="technical"),
    re_path(r"^words|mots$", words, name="words"),
    re_path("^word|mot/(?P<word>.*)/$", word_detail, name="word"),
]
