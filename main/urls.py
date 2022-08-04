from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("/lihat", views.lihat, name="lihat"),
    path("/about", views.about, name="about"),
]
