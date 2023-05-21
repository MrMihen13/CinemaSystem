from django.urls import path

from movie import views

urlpatterns = [
    path('movie/<int:pk>', views.MovieRetrieveAPIView.as_view()),
    path('movie', views.MoviesListAPIView.as_view()),
    path('movie/popular', views.PopularMovieListAPIView.as_view()),
    path('genre', views.GenreListAPIView.as_view()),
]
