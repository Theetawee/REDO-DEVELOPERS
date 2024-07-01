from django.conf import settings
from django.utils import timezone


def app(request):
    data = {"APP_NAME": settings.APP_NAME, "year": timezone.now().year}
    return data
