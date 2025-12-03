from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_semanas, name="metas"),
    path("/create/",views.create_meta, name="create_meta")

]
