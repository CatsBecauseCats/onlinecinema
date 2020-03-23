'''
from django import template
from django.views import View
from django.db.models import Sum
from django.utils import timezone

from knowledge.models import FilmStatistic

register = template.Library()


@register.simple_tag
def get_popular_movies_for_week():

    popular = FilmStatistic.objects.filter(
        date__range=[timezone.now() - timezone.timedelta(7), timezone.now()]
    ).values(
        'film_name', 'creator_name'
    ).annotate(
        views=Sum('views')
    ).order_by(
        '-views')[:5]

    return popular
'''