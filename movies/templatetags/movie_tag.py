from django import template
from movies.models import Country, Request


register = template.Library()


@register.simple_tag()
def get_categories():
    """Вывод всех категорий"""
    return Country.objects.all()
#
#
@register.simple_tag()
def get_request():
    """Вывод всех категорий"""
    return Request.objects.all()
#
# # @register.inclusion_tag('movies/tags/last_movie.html')
# # def get_last_movies(count=5):
# #     movies = Movie.objects.order_by("id")[:count]
# #     return {"last_movies": movies}