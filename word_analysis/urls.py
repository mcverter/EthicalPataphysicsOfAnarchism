from django.urls import re_path

from .views import debug_test, word_detail, word_list, technical, summary, relations, \
    genre_list, genre_detail, content_page

urlpatterns = [
    # Index
    re_path(r"^$", summary, name="summary"),
    # Top-Level Pages
    re_path(r"^summary|resume$", summary, name="summary"),
    re_path(r"^relations$", relations, name="relations"),
    re_path(r"^technical|technique$", technical, name="technical"),
    re_path(r"^debug_test$", debug_test, name="debug_test"),

    # List and Detail Views
    re_path(r"^words|mots$", word_list, name="words"),
    re_path("^words|mots/(?P<prefix>.*)/$", word_list, name="words"),
    re_path("^mot/(?P<word>.*)/$", word_detail, name="word"),
    re_path("^word/(?P<word>.*)/$", word_detail, name="word"),
    re_path(r"^genres$", genre_list, name="genre_list"),
    re_path("^genre/(?P<word>.*)/$", genre_detail, name="genre_detail"),

    # Content Pages
    re_path("^abstract$", content_page, {"name": "abstract"}),
    re_path("^addition$", content_page, {"name": "addition"}),
    re_path("^combination$", content_page, {"name": "combination"}),
    re_path("^constellation$", content_page, {"name": "constellation"}),
    re_path("^(curvature|courbure)$", content_page, {"name": "curvature"}),
    re_path("^(deux|duality|two)$", content_page, name="duality"),
    re_path("^euclid$", content_page, {"name": "euclid"}),
    re_path("^flat$", content_page, {"name": "flat"}),
    re_path("^intersection$", content_page, {"name": "intersection"}),
    re_path("^numbers$", content_page, {"name": "numbers"}),
    re_path("^objective$", content_page, {"name": "objective"}),
    re_path("^opposition$", content_page, {"name": "opposition"}),
    re_path("^parallelism$", content_page, {"name": "parallelism"}),
    re_path("^repetition$", content_page, {"name": "repetition"}),
    re_path("^two_dimensional$", content_page, {"name": "two_dimensional"}),

    re_path("^definition$", content_page, name="definition"),
    re_path("^etymology$", content_page, name="etymology"),
    re_path("^(un|one)$", content_page, name="un"),
    re_path("^(zero|null)$", content_page, name="zero"),
    re_path("^(trois|three)$", content_page, name="trois"),
    re_path("^perversion$", content_page, name="perversion"),
    re_path("^inversion$", content_page, name="inversion"),
    re_path("^subversion$", content_page, name="subversion"),
    re_path("^reversion$", content_page, name="reversion"),
    re_path("^(quatre|four|square|carre)$", content_page, name="four"),
    re_path("^perspectivism$", content_page, name="perspectivism"),

    # TODO: move these to BCP
]

'''
zzzzzt
debug_test.html         genre_list_page.html  relations_page.html  technical_page.html            word_detail_page.html
genre_detail_page.html    summary_page.html    content_page.html  word_list_page.html



addition.html 

'''
