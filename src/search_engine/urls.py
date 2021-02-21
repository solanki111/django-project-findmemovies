from django.urls import path, re_path

from .views import (
    discover,
    popular,
    similar_movie,
    similar_tv,
    movie,
    search,
    tv,
    trending
)

app_name = 'search_engine'
urlpatterns = [
    path('discover/movies', discover, name='discover-movies'),
    path('popular/movies', popular, name='popular-movies'),
    path('search/movies', search, name='search-movies'),
    path('search/movies/<slug:movie_id>', movie, name='get-movie'),
    path('similar/movies/<slug:movie_id>', similar_movie, name='similar-movies'),
    path('search/tv/<slug:tv_id>', tv, name='get-tv'),
    path('similar/tv/<slug:tv_id>', similar_tv, name='similar-tv'),
    path('trending/movies', trending, name='trending-movies')
]