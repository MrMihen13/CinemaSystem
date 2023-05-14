from django.urls import path

from cinema import views

urlpatterns = [
    path("cinema/<int:pk>", views.CinemaRetrieveAPIView.as_view()),
    path('cinema', views.CinemaListAPIView.as_view())
]
