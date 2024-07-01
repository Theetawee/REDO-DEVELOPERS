from django.conf import settings
from .models import IPGeolocation
import requests
from .utils import get_client_ip


def app(request):
    ip = get_client_ip(request)

    try:
        ip_geolocation = IPGeolocation.objects.get(ip=ip)
        data = {
            "APP_NAME": settings.APP_NAME,
            "location": ip_geolocation,
        }
    except IPGeolocation.DoesNotExist:
        try:
            url = f"https://ipapi.co/{ip}/json/"  # API endpoint for IP geolocation
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                # Save fetched data to the database
                ip_geolocation = IPGeolocation.objects.create(
                    ip=ip,
                    city=data.get("city", ""),
                    country=data.get("country_name", ""),
                    country_code=data.get("country", ""),
                    latitude=data.get("latitude", 0),
                    longitude=data.get("longitude", 0),
                    timezone=data.get("timezone", ""),
                )
                ip_geolocation.save()
                data = {
                    "APP_NAME": settings.APP_NAME,
                    "location": ip_geolocation,
                }
            else:
                data = {
                    "APP_NAME": settings.APP_NAME,
                    "location": ip,
                }
        except requests.RequestException as e:
            print(f"Error fetching IP data: {e}")
            data = {
                "APP_NAME": settings.APP_NAME,
                "location": ip,
            }

    return data
