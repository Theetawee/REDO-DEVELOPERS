from django.shortcuts import render
from .models import Testimony


# Create your views here.
def index(request):
    testimonies = Testimony.objects.all()
    context = {"testimonies": testimonies}
    return render(request, "main/index.html", context)
