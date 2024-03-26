from django.shortcuts import render
from .models import Testimony


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
    context = {
        "title": "Profiles | Redo Developers Inc.",
        "description": "Discover a transformative partnership with Redo Developers Inc. We're your trailblazing ally, delivering cutting-edge technology and innovative software solutions to propel businesses and individuals towards success in the dynamic digital landscape.",
    }

    return render(request, "main/profiles.html", context)
