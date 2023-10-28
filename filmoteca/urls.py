from django.urls import re_path, path
from . import views

urlpatterns = [
    re_path(r'^$',views.index, name='index'),
    path(r'director/<str:director>',views.director.director, name='director'),
    path(r'getDirectors/', views.getDirectors.as_view(), name='getDirectors'),
]
