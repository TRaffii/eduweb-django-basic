from django.shortcuts import render

# Create your views here.
from .models import Movie


def show_movies(request):
    movies = Movie.objects.all()
    return render(request, 'index_movies.html', {'movies': movies})
