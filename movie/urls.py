from django.urls import path

from movie import views

urlpatterns = [
    path('movie/<int:pk>', views.MoveRetrieveAPIView.as_view()),
    path('movie', views.MoviesListAPIView.as_view())
]
