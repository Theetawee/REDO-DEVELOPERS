from django.shortcuts import render, get_object_or_404
from .models import Testimony
from .models import CompanyProfile


# Create your views here.
def index(request):
    testimonies = Testimony.objects.all()
    context = {
        "testimonies": testimonies,
        "title": "Redo Developers Inc. | Pioneering Technology Solutions for Success",
        "description": "Discover a transformative partnership with Redo Developers Inc. We&#x27;re your trailblazing ally, delivering cutting-edge technology and innovative software solutions to propel businesses and individuals towards success in the dynamic digital landscape.",
    }
    return render(request, "main/index.html", context)


def about_company(request):
    context = {
        "title": "About Redo Developers Inc. | Pioneering Innovation in Software and Technological services.",
        "description": "Explore the journey of Redo Developers Inc. – where vision meets innovation. Learn about our commitment to reshaping the digital landscape, crafting software solutions that transcend boundaries, and our impact on industries and society.",
    }
    return render(request, "main/about.html", context)


def company_profiles(request):
    profiles = CompanyProfile.objects.all()
    context = {
        "title": "Profiles | Redo Developers Inc.",
        "description": "Discover a transformative partnership with Redo Developers Inc. We're your trailblazing ally, delivering cutting-edge technology and innovative software solutions to propel businesses and individuals towards success in the dynamic digital landscape.",
        "profiles": profiles,
    }

    return render(request, "main/profiles.html", context)


def profile_detail(request, slug):
    profile = get_object_or_404(CompanyProfile, slug=slug)
    context = {"profile": profile}
    return render(request, "main/profile_detail.html", context)


def company_services(request):
    return render(request, "main/services.html")
