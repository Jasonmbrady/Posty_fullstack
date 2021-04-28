from django.shortcuts import render, redirect
from .models import User, Task
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
        "all_tasks": Task.objects.all(),
    }
    return render(request, "dashboard.html", context)

def new_task(request):
    return render(request, 'new_task.html')

def create_task(request):
    t_name = request.POST['task_name']
    t_cat = request.POST['category']
    Task.objects.create(task_name=t_name, category=t_cat)
    return redirect("/dashboard")

def add_task(request, id):
    this_user = User.objects.get(id=request.session['uid'])
    this_user.tasks.add(Task.objects.get(id=id))
    return redirect("/dashboard")

def remove_task(request, id):
    this_task = Task.objects.get(id=id)
    this_task.delete()
    return redirect("/dashboard")

def abandon(request, id):
    this_user = User.objects.get(id=request.session['uid'])
    this_user.tasks.remove(Task.objects.get(id=id))
    return redirect("/dashboard")

def complete(request, id):
   this_task = Task.objects.get(id=id)
   this_task.completed = True
   this_task.save()
   return redirect("/dashboard")
