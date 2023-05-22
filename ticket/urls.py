from django.urls import path

from ticket import views

urlpatterns = [
    path('ticket', views.TicketCreateAPIView.as_view()),
    path('tickets', views.TicketListAPIView.as_view()),
    path('ticket/<int:pk>', views.TicketRetrieveUpdateDestroyAPIView.as_view()),
]
