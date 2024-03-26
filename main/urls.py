from django.urls import path
from .views import index, about_company


urlpatterns = [
    path("", index, name="home"),
    path("about/", about_company, name="about"),
]
