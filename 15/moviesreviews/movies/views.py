from django.shortcuts import render

# Create your views here.
from .forms import ReviewForm
from .models import Movie


def show_movies(request):
    movies = Movie.objects.all()
    return render(request, 'index_movies.html', {'movies': movies})


def add_review(request):
    form = ReviewForm()
    context = {
        'form': form
    }
    return render(request, "add_review.html", context)