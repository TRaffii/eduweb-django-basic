from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from .forms import ReviewForm
from .models import Movie, Review


def show_movies(request):
    movies = Movie.objects.all()
    return render(request, 'index_movies.html', {'movies': movies})


def add_review(request):
    if not request.user.is_authenticated:
        return redirect("index")
    form = ReviewForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("index")
    context = {
        'form': form
    }
    return render(request, "add_review.html", context)


def show_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    reviews = Review.objects.filter(movie=movie)

    context = {
        'movie': movie,
        'reviews': reviews,
        'error': None
    }

    return render(request, "show_movie.html", context)
