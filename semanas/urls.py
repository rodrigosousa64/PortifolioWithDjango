from django.urls import path
from . import views

urlpatterns = [
    path("", views.semanas, name="metas"),
    path("/create", views.create_meta, name="create_meta"),
    path("/toggle/<int:id>", views.toggle, name="toggle"),
]
