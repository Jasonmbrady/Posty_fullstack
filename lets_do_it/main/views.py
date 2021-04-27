from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, "index.html")

def login(request):
    errors = User.objects.login_validator(request.POST)
    if errors:
        for key, val in errors.items():
            messages.error(request, val)
        return redirect("/")
    else:
        this_user = User.objects.get(username = request.POST['username'])
        request.session['uid'] = this_user.id
    return redirect("/dashboard")

def registration(request):
    return render(request, "register.html")

def register(request):
    errors = User.objects.register_validator(request.POST)
    if errors:
        for key, val in errors.items():
            messages.error(request, val)
        return redirect("/registration")
    else:
        u_name = request.POST['username']
        pwd = request.POST['password']
        this_user = User.objects.create(username=u_name, password = pwd)
        request.session['uid'] = this_user.id
        return redirect("/dashboard")

def dashboard(request):
    context = {
        "this_user": User.objects.get(id=request.session['uid']),
    }
    return render(request, "dashboard.html", context)