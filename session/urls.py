from django.urls import path

from session import views

urlpatterns = [
    path('sessions', views.ListSessionAPIView.as_view())
]
