from django.urls import re_path

from .views import debug_test, word_detail, word_list, translation_content_page, technical, summary, relations, \
    genre_list, genre_detail

'''

debug_test.html         genre_list_page.html  relations_page.html  technical_page.html            word_detail_page.html
genre_detail_page.html    summary_page.html    translation_content_page.html  word_list_page.html


  
addition.html 
  
'''
urlpatterns = [
    re_path(r"^words|mots$", word_list, name="words"),
    re_path("^words|mots/(?P<prefix>.*)/$", word_list, name="words"),
    re_path("^word|mot/(?P<word>.*)/$", word_detail, name="word"),
    re_path(r"^genres|genres$", genre_list, name="genre_list"),
    re_path("^genre|genre/(?P<word>.*)/$", genre_detail, name="genre_detail"),

    re_path(r"^$", summary, name="summary"),
    re_path("^abstract$", translation_content_page, name="abstract"),
    re_path("^addition$", translation_content_page, name="addition"),
    re_path("^combination$", translation_content_page, name="combination"),
    re_path("^constellation$", translation_content_page, name="constellation"),
    re_path("^(curvature|courbure)$", translation_content_page, name="constellation"),
    re_path("^(deux|duality|two)$", translation_content_page, name="duality"),
    re_path("^euclid$", translation_content_page, name="euclid"),
    re_path("^flat$", translation_content_page, name="flat"),
    re_path("^intersection$", translation_content_page, name="intersection"),
    re_path("^numbers$", translation_content_page, name="numbers"),
    re_path("^objective$", translation_content_page, name="objective"),
    re_path("^opposition$", translation_content_page, name="opposition"),
    re_path("^parallelism$", translation_content_page, name="parallelism"),
    re_path("^definition$", translation_content_page, name="definition"),
    re_path("^etymology$", translation_content_page, name="etymology"),
    re_path("^two_dimensional$", translation_content_page, name="two_dimensional"),
    re_path("^(un|one)$", translation_content_page, name="un"),
    re_path("^(zero|null)$", translation_content_page, name="zero"),
    re_path("^(trois|three)$", translation_content_page, name="trois"),
    re_path("^perversion$", translation_content_page, name="perversion"),
    re_path("^inversion$", translation_content_page, name="inversion"),
    re_path("^subversion$", translation_content_page, name="subversion"),
    re_path("^reversion$", translation_content_page, name="reversion"),
    re_path("^(quatre|four|square|carre)$", translation_content_page, name="four"),
    re_path("^perspectivism$", translation_content_page, name="perspectivism"),

    # TODO: move these to BCP
    re_path(r"^relations$", relations, name="relations"),
    re_path(r"^summary|resume$", summary, name="summary"),
    re_path(r"^technical|technique$", technical, name="technical"),

    re_path(r"^debug_test$", debug_test, name="debug_test"),
]
