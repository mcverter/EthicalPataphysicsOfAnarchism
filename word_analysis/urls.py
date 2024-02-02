from django.urls import re_path

from .views import (
    debug_test,
    word_detail,
    word_list,
    technical,
    summary,
    genre_theory,
    genre_list,
    genre_detail,
    content_page,
    topics
)

urlpatterns = [
    # Index
    re_path(r"^$", summary, name="summary"),

    # Top-Level Pages
    re_path(r"^summary", summary, name="summary"),
    re_path(r"^resume", summary, name="resume"),
    re_path(r"^genre_theory", genre_theory, name="genre_theory"),
    re_path(r"^topics", topics, name="topics"),

    re_path(r"^technical", technical, name="technical"),
    re_path(r"^technique", technical, name="technique"),

    # List and Detail Views
    re_path(r"^words", word_list, name="words"),
    re_path(r"^mots", word_list, name="mots"),
    re_path("^mot/(?P<word>.*)/$", word_detail, name="word"),
    re_path("^word/(?P<word>.*)/$", word_detail, name="mot"),
    re_path(r"^genres", genre_list, name="genres"),
    re_path("^genre/(?P<word>.*)/$", genre_detail, name="genre_detail"),

    # Content Pages
    re_path("^abstract", content_page, {"name": "abstract"}),
    re_path("^plus_one", content_page, {"name": "plus_one"}),
    re_path("^objective", content_page, {"name": "objective"}),
    re_path("^ambisexuality", content_page, {"name": "ambisexuality"}),
    re_path("^home_and_position", content_page, {"name": "home_and_position"}),
    re_path("^womb", content_page, {"name": "womb"}),
    re_path("^hostage", content_page, {"name": "hostage"}),
    re_path("^two_dimensional", content_page, {"name": "two_dimensional"}),
    re_path("^discussion", content_page, {"name": "discussion"}),
    re_path("^flat", content_page, {"name": "flat"}),
    re_path("^three", content_page, {"name": "three"}),
    # Genre Theory Page
    re_path("^combination", content_page, {"name": "combination"}),
    re_path("^constellation", content_page, {"name": "constellation"}),
    re_path("^(curvature|courbure)", content_page, {"name": "curvature"}),
    re_path("^(deux|duality|two)", content_page, name="duality"),
    re_path("^euclid", content_page, {"name": "euclid"}),
    re_path("^flat", content_page, {"name": "flat"}),
    re_path("^intersection", content_page, {"name": "intersection"}),
    re_path("^numbers", content_page, {"name": "numbers"}),
    re_path("^objective", content_page, {"name": "objective"}),
    re_path("^opposition", content_page, {"name": "opposition"}),
    re_path("^parallelism", content_page, {"name": "parallelism"}),
    re_path("^repetition", content_page, {"name": "repetition"}),
    re_path("^two_dimensional", content_page, {"name": "two_dimensional"}),
    re_path("^definition", content_page, name="definition"),
    re_path("^etymology", content_page, name="etymology"),
    re_path("^(un|one)", content_page, name="un"),
    re_path("^(zero|null)", content_page, name="zero"),
    re_path("^(trois|three)", content_page, name="trois"),
    re_path("^perversion", content_page, name="perversion"),
    re_path("^inversion", content_page, name="inversion"),
    re_path("^subversion", content_page, name="subversion"),
    re_path("^reversion", content_page, name="reversion"),
    re_path("^(quatre|four|square|carre)", content_page, name="four"),
    re_path("^perspectivism", content_page, name="perspectivism"),

    # Debug Page
    re_path(r"^debug_test", debug_test, name="debug_test"),
]
