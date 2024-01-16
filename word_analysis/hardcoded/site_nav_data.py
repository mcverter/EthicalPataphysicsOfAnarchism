nav_items = [
    {"route": "summary", "title": "Project Summary"},
    {"route": "mots", "title": "Word list"},
    {"route": "genres", "title": "Genre Sets (GS)"},
    {"route": "relations", "title": "Internal and external relations",
     "subitems": [
         {"route": "duality", "title": "duality"},
         {"route": "combination", "title": "combination"},
         {"route": "parallelism", "title": "parallelism"},
         {"route": "intersection", "title": "intersection"},
         {"route": "flat", "title": "flat"},
         {"route": "two_dimensional", "title": "two_dimensional"},
     ]},
    {"route": "technical", "title": "Technical notes"},
]

'''

----                 -------------         ------ ----
-a----         1/15/2024  12:11 PM           3084 abstract.html
-a----          1/9/2024  11:20 AM             24 addition.html
-a----         1/15/2024  12:11 PM           1057 combination.html
-a----         1/15/2024   6:56 AM           7571 constellation.html
-a----         1/15/2024   3:21 PM              9 curvature.html
-a----          1/9/2024  11:20 AM          11873 duality.html
-a----          1/9/2024  11:20 AM           1765 flat.html
-a----          1/9/2024  11:20 AM            267 intersection.html
-a----          1/9/2024  11:20 AM             56 numbers.html
-a----         1/15/2024  12:10 PM           1721 objective.html
-a----         1/15/2024   5:28 AM           3790 objectivebackup.html
-a----          1/9/2024  11:20 AM           1203 opposition.html
-a----          1/9/2024  11:20 AM            970 parallelism.html
-a----         1/15/2024   5:27 PM           3726 repetition.html
-a----          1/9/2024  11:20 AM           4279 two_dimensional.html

'''

'''
   re_path(r"^words|mots$", word_list, name="words"),
    re_path("^words|mots/(?P<prefix>.*)/$", word_list, name="words"),
    re_path("^word|mot/(?P<word>.*)/$", word_detail, name="word"),
    re_path(r"^genres|genres$", genre_list, name="genre_list"),
    re_path("^genre|genre/(?P<word>.*)/$", genre_detail, name="genre_detail"),

    re_path(r"^$", summary, name="summary"),
    re_path("^abstract$", content_page, {"name": "abstract"}),
    re_path("^addition$", content_page, {"name": "addition"}),
    re_path("^combination$", content_page, {"name": "combination"}),
    re_path("^constellation$", content_page, {"name": "constellation"}),
    re_path("^(curvature|courbure)$", content_page, {"name": "constellation"}),
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
    re_path(r"^relations$", relations, name="relations"),
    re_path(r"^summary|resume$", summary, name="summary"),
    re_path(r"^technical|technique$", technical, name="technical"),

    re_path(r"^debug_test$", debug_test, name="debug_test"),
]
'''
