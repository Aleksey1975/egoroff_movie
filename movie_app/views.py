from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import *
from django.db.models import F, Sum, Max, Min, Count, Avg, Value


def index(request):
    movies = Movie.objects.order_by(F('rating').desc(nulls_first=True), 'budget')
    # movies = Movie.objects.annotate(new=Value(True),
    #                                 new_budget=F('budget') + 99,
    #                                 r_plus_y=F('rating') + F('year'))
    stat = movies.aggregate(Avg('budget'), Max('rating'))
    for movie in movies:
        movie.save()
    context = {
        'title': 'Фильмы',
        'movies': movies,
        'stat': stat
    }
    return render(request, 'movie_app/index.html', context=context)


def show_one_movie(request, movie_slug: str):
    movie = get_object_or_404(Movie, slug=movie_slug)
    context = {
        'title': 'Фильм',
        'movie': movie
    }
    return render(request, 'movie_app/one_movie.html', context=context)
