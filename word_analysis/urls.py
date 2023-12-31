from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings
from .views import word_detail, words, groups, technical, summary, relations

urlpatterns = [
                  re_path(r"^$", summary, name="summary"),
                  re_path(r"^relations$", relations, name="relations"),
                  re_path(r"^membership$", membership, name="membership"),
                  re_path(r"^summary|resume$", summary, name="summary"),
                  re_path(r"^groups|groupes$", groups, name="groups"),
                  re_path(r"^technical|technique$", technical, name="technical"),
                  re_path(r"^words|mots$", words, name="words"),
                  path("mot/<str:word>/", word_detail, name="word"),
                  path("word/<str:word>/", word_detail, name="word"),

                  # re_path(r"^articles/(?P<year>[0-9]{4})/$", views.year_archive),
                  # cre_path("^word|mot/(?P<word>[.*])", word_detail, name="word"),
                  # re_path(r"^confirm-email/(?P<key>[-:\w]+)/$", views.confirm_email, name="account_confirm_email"),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
