from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("filter/", views.FilterMoviesView.as_view(), name='filter'),
    path('films/', views.FilmListView.as_view(), name='films'),
    path('person', views.PersonsListView.as_view(), name='person'),
    path('popular-films/', views.PopularFilmListView.as_view(), name='popular-films'),
]