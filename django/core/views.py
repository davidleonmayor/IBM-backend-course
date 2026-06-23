import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password, check_password
from .models import User


@csrf_exempt
def signup(request):
    if request.method != "POST":
        return JsonResponse({"error": "Method not allowed"}, status=405)

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    names = data.get("names", "").strip()
    last_names = data.get("last_names", "").strip()
    email = data.get("email", "").strip()
    password = data.get("password", "")

    if not all([names, last_names, email, password]):
        return JsonResponse({"error": "All fields are required"}, status=400)

    if User.objects.filter(email=email).exists():
        return JsonResponse({"error": "Email already registered"}, status=400)

    user = User.objects.create(
        names=names,
        last_names=last_names,
        email=email,
        password=make_password(password),
    )

    return JsonResponse({
        "id": user.id,
        "names": user.names,
        "last_names": user.last_names,
        "email": user.email,
    }, status=201)


@csrf_exempt
def login(request):
    if request.method != "POST":
        return JsonResponse({"error": "Method not allowed"}, status=405)

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    email = data.get("email", "").strip()
    password = data.get("password", "")

    if not all([email, password]):
        return JsonResponse({"error": "Email and password are required"}, status=400)

    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return JsonResponse({"error": "Invalid credentials"}, status=401)

    if not check_password(password, user.password):
        return JsonResponse({"error": "Invalid credentials"}, status=401)

    return JsonResponse({
        "id": user.id,
        "names": user.names,
        "last_names": user.last_names,
        "email": user.email,
    })
