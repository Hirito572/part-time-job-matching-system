"""Views for the core application."""

from django.http import JsonResponse


def health_check(_request):
    """Return the API health status."""
    return JsonResponse({
        "status": "ok",
        "message": "Part-Time Job Matching API is running",
    })
