from django.shortcuts import render
from django.views import generic
from .models import Persona, Film, MovieViewsPerWeek
from datetime import timedelta, datetime

def index(request):

    return render(
        request,
        'index.html',
    )

class DirectorYearActor:
    def get_director(self):
        return Film.objects.all()
    def get_actors(self):
        return Film.objects.all()
    def get_year(self):
        return Film.objects.filter(default=True).values()

class FilmView(DirectorYearActor, generic.ListView):
    model = Film
    queryset = Film.objects.filter().values("creator_name")
    paginate_by = 2

class FilmListView(DirectorYearActor, generic.ListView):
    model = Film
    #queryset = Film.objects.filter(draft=True)
    paginate_by = 2

class PopularFilmListView(DirectorYearActor, generic.ListView):
    model = MovieViewsPerWeek

class PersonsListView(generic.ListView):
    model = Persona

# Здесь пока только фильтрация по режиссеру(вылетает ошибка)
# Пока нет фильтрации по актеру и году, поскольку это  будеет выглядеть похожим образом
# Вопрос: как сделать при выводе в httml чекбокс-режиссер уникальным?
class FilterMoviesView(DirectorYearActor, generic.ListView):
    def get_queryset(self):
        queryset = Film.objects.filter(
            creator_name__in=self.request.GET.getlist("creator_name"))
        return queryset

# Попытка убрать повтрорения из чекбокса
class UnicCreator(generic.ListView):
    model = Film
    context_object_name = 'creator_name'
    template_name = "cinema/film_list.html"

    def get_queryset(self):
        return Film.objects.order_by().values('creator_name').distinct()

# Не работает совсем (вывод N самых популярных фильмов за последние 4 недели)
'''
class FilterFilmListView(generic.ListView):
    model = Film
    context_object_name = 'count_views'
    now = datetime.now() - timedelta(minutes=60 * 24 * 30) # Берем данные за последний месяц
    films = Film.objects.filter(created__gte=now) # Вылетает тут - нужно будет для запуска обернуть в movieviewsperweek_list
                                                  # строки 7-9 в <form action="{% url 'filter' %}" method="get"><form/>
    queryset = Film.objects.filter()[:5]  # Получение 5 просмотренных фильмов
                                          # (в дальнейшем вместо 5 будет N, берущееся из поля по нажатию кнопки
                                          # в movieviewsperweek_list.html)
    template_name = 'cinema/movieviewsperweek_list.html'  # Определение имени шаблона и его расположения
'''