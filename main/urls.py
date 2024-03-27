from django.urls import path
from .views import (
    index,
    about_company,
    company_profiles,
    profile_detail,
    company_services,
)


urlpatterns = [
    path("", index, name="home"),
    path("company/about/", about_company, name="about"),
    path("company/profiles/", company_profiles, name="profiles"),
    path("company/profiles/<slug:slug>/", profile_detail, name="detail"),
    path("services/", company_services, name="products"),
]
