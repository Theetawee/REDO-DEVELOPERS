from django.shortcuts import render
from .models import IPGeolocation


class BlockIPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get client's IP address
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        ip_address = (
            x_forwarded_for.split(",")[0]
            if x_forwarded_for
            else request.META.get("REMOTE_ADDR")
        )

        # Check if IP is blocked
        try:
            ip_geolocation = IPGeolocation.objects.get(ip=ip_address)
            if ip_geolocation.blocked:
                return render(request, "base/blocked.html", status=403)
        except IPGeolocation.DoesNotExist:
            pass

        response = self.get_response(request)
        return response
