from django.http import HttpRequest


def get_client_ip(request: HttpRequest) -> str:
    # Assuming the request object is available
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip
