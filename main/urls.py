from django.urls import path
from .views import (
    index,
    about_company,
    company_profiles,
    profile_detail,
    company_services,
    contact_us,
    investments
)


urlpatterns = [
    path("", index, name="home"),
    path("about-company/", about_company, name="about"),
    path("company/profiles/", company_profiles, name="profiles"),
    path("company/profiles/<slug:slug>/", profile_detail, name="detail"),
    path("services/", company_services, name="services"),
    path("contact/", contact_us, name="contact"),
    path("investments/", investments, name="investments"),
]
