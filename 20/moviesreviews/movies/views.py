from django.shortcuts import render, redirect

# Create your views here.
from .forms import ReviewForm
from .models import Movie, Review


def show_movies(request):
    movies = Movie.objects.all()
    return render(request, 'index_movies.html', {'movies': movies})


def add_review(request):
    form = ReviewForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("index")
    context = {
        'form': form
    }
    return render(request, "add_review.html", context)


def show_movie(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    reviews = Review.objects.filter(movie=movie)

    context = {
        'movie': movie,
        'reviews': reviews
    }

    return render(request, "show_movie.html", context)
