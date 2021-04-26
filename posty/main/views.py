from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt


# Create your views here.
def index(request):
    return render(request, "index.html")

def add_user(request):
    errors = User.objects.user_validator(request.POST)
    if len(errors) > 0:
        for key, val in errors.items():
            messages.error(request, val)
        return redirect("/")
    else:
        new_name = request.POST["name"]
        new_email = request.POST["email"]
        new_pass = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        new_user = User.objects.create(name=new_name, email=new_email, password=new_pass)
        request.session['username'] = new_user.name
        request.session['uid'] = new_user.id
        return redirect("/chat")

def chat(request):
    context = {
        "all_posts": Post.objects.all(),
        "this_user": User.objects.get(id=request.session['uid'])
    }
    return render(request, "chat.html", context)

def login_page(request):
    return render(request, "login.html")

def login(request):
    this_name = request.POST['name']
    users = User.objects.filter(name=this_name)
    if users:
        this_user = users[0]
        if bcrypt.checkpw(request.POST['password'].encode(), this_user.password.encode()):
            request.session['username'] = this_user.name
            request.session['uid'] = this_user.id
            return redirect("/chat")
    return redirect("/login_page")

def new_post(request):
    posting_user = User.objects.get(id=request.session['uid'])
    post_text = request.POST['text']
    Post.objects.create(text = post_text, poster = posting_user)
    return redirect("/chat")

def edit_post(request, id):
    context = {

        "this_post": Post.objects.get(id=id)
    }
    return render(request, "edit.html", context)

def update_post(request):
    this_post_id = request.POST['id']
    post_to_update = Post.objects.get(id = this_post_id)
    post_to_update.text = request.POST['edited_text']
    post_to_update.save()
    return redirect("/chat")

def delete_post(request, id):
    post_to_delete = Post.objects.get(id=id)
    post_to_delete.delete()
    return redirect("/chat")

def logout(request):
    request.session.flush()
    return redirect("/")

def add_favorite(request, post_id):
    this_post = Post.objects.get(id=post_id)
    this_post.favorite_of.add((User.objects.get(id=request.session['uid'])))
    return redirect("/chat")