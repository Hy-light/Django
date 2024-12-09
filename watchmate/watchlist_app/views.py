from django.shortcuts import render
from watchlist_app.models import Movie
from django.http import JsonResponse

# Create your views here. Views are used to pull data from the database and return it to the client.

# List all movies
def movie_list(request):
    movies = Movie.objects.all()
    data = {
        'movies': list(movies.values())
    }
    return JsonResponse(data)
    
# List particular movie details 
def movie_detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    data = {
        'movie': movie.name,
        'description': movie.description,
        'active': movie.active
    }
    return JsonResponse(data)
    