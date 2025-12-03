from django.urls import path
from . import views

urlpatterns = [
    path("", views.draws_home, name="home_draws"),
    
]
