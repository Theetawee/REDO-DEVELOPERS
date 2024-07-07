from django.urls import path
from .views import (
    index,
    about_company,
    company_profiles,
    profile_detail,
    company_services,
    contact_us,
    carrers_view,
    investor_relations,
)


urlpatterns = [
    path("", index, name="home"),
    path("about-company/", about_company, name="about"),
    path("company/leadership/", company_profiles, name="leadership"),
    path("company/profiles/<slug:slug>/", profile_detail, name="profile_detail"),
    path("services/", company_services, name="services"),
    path("contact/", contact_us, name="contact"),
    path("carrers/", carrers_view, name="carrers"),
    path("ir/", investor_relations, name="investors"),
]
