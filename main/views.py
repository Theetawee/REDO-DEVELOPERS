from django.shortcuts import render
from django.http import HttpResponse
import os
from django.template import loader
from pathlib import Path
from django.views.generic import View







# Create your views here.
def index(request):
    return render(request, "main/index.html")
