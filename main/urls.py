from django_distill import distill_path as path
from django.urls import path as url
from .views import (
    index,
    about_company,
    company_profiles,
    profile_detail,
    company_services,
    contact_us,
    carrers_view,
)


urlpatterns = [
    path("", index, name="home"),
    path("about-company/", about_company, name="about"),
    path("company/profiles/", company_profiles, name="profiles"),
    url("company/profiles/<slug:slug>/", profile_detail, name="detail"),
    path("services/", company_services, name="services"),
    path("contact/", contact_us, name="contact"),
    path("carrers/", carrers_view, name="carrers"),
]
