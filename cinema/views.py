from django.shortcuts import render
from django.views import generic
from .models import Persona, Film, MovieViewsPerWeek


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

class FilterMoviesView(DirectorYearActor, generic.ListView):
    """Фильтр фильмов"""

    def get_queryset(self):
        queryset = Film.objects.filter(
            creator_name__in=self.request.GET.getlist("creator_name"))
        return queryset
    '''
    def get_queryset(self):
        return Film.objects.filter(year=1992)[:4]
    '''
'''
def film_filter(request, pk):
    """ Фильтр статей по дате
    """
    films = PopularFilmListView.object_list()
    if pk == 2:
        now = datetime.now() - timedelta(minutes=60 * 24 * 30)
        films = films.filter(created__gte=now)

    return render(request, "cinema/movieviewsperweek_list.html", {"films": films})
'''


'''
def my_filter(self, id_button):
    film = Film.objects.all()
    if id_button == 1:
        now = datetime.now() - timedelta(minutes=60 * 24 * 7)
        film = film.filter(created__gte=now)
    elif id_button == 2:
        now = datetime.now() - timedelta(minutes=60 * 24 * 30)
        news = film.filter(created__gte=now)
    elif id_button == 3:
        news = film

    return render(self.request, "news/news_list.html", {"news": news})
'''

#Book.objects.filter(title__icontains='war')[:5]  # Получить 5 книг, содержащих 'war' в заголовке