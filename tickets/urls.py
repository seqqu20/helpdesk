
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('nowe/', views.create_ticket, name='create_ticket'),
    path('sprawdz/', views.lookup_ticket, name='lookup_ticket'),
]
