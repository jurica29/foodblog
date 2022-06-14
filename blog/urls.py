from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),

    path('specific', views.specific, name='specific'),

    path('search', views.search, name="search"),

    path('articles', views.articles, name="articles"),

    path('contact', views.contact, name="contact")
]