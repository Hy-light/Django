from django.urls import path, include
from watchlist_app.api.views import MovieListAV, MovieDetailAV

urlpatterns = [
    # Add your URL patterns here.
    path('list/', MovieListAV.as_view(), name='movie-list' ),
    path('<int:pk>', MovieDetailAV.as_view(), name='movie-detail' ),  # Add this line to create a detail view for each movie.
    
]