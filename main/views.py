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
