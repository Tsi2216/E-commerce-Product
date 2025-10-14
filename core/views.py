from django.http import JsonResponse

def home(request):
    return JsonResponse({
        "message": "Welcome to the E-commerce API!",
        "endpoints": {
            "products": "/api/products/",
            "users": "/api/users/",
            "token_obtain": "/api/token/",
            "token_refresh": "/api/token/refresh/"
        }
    })
