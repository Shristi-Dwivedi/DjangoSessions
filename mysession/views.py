from django.contrib.auth import authenticate,login
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is None:
            return JsonResponse({"error":"Invalid Credentials"}, status=401)
        
        login(request, user)

        # Expire user after 10 seconds
        request.session.set_expiry(10)
        return redirect("dashboard")

    return render(request, "login.html")

@login_required
def dashboard(request):
    return HttpResponse(f"Welcome {request.user.username} to your dashboard")