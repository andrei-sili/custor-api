from django.http import JsonResponse

def health(request):
    return JsonResponse({
        "status": "ok",
        "project": "custor-api",
        "version": "0.1.0"
    })

