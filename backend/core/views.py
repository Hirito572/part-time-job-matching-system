
from django.http import JsonResponse


def health_check(request):
    return JsonResponse({
        "status": "ok",
        "message": "Part-Time Job Matching API is running"
    })
