from django.urls import path
from .views import mot_detail, index

urlpatterns = [
    path("", index, name="index"),
    path("word/<str:word>/", mot_detail, name="word"),
    path("mot/<str:word>/", mot_detail, name="mot"),
]
