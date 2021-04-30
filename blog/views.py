from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, LoginForm, BlogForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Blogs
# Create your views here.

def Home(request):
    posts = Blogs.objects.all()
    return render(request, 'home.html', {'posts':posts})

def About(request):

    return render(request, 'about.html')

def Contact(request):

    return render(request, 'contact.html')

def Dashboard(request):
    if request.user.is_authenticated:
        posts = Blogs.objects.all()
        return render(request, 'dashboard.html', {'posts':posts})
    else:
        return HttpResponseRedirect('/login')

def User_Logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def User_Signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Welcome...!!')
            form.save()
            return HttpResponseRedirect('/login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form':form})

def User_Login(request):
    if not request.user.is_authenticated:
        if request.method =="POST":
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Welcome Back...!!')
                    return HttpResponseRedirect('/dashboard')
                else:
                    messages.success(request, 'Opps something has gone wrong !!!')
                    return HttpResponseRedirect('/login')
        else:
            form = LoginForm()
        return render(request, 'login.html', {'form':form})
    else:
        return HttpResponseRedirect('/dashboard')

def Add_blog(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = BlogForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                dis = form.cleaned_data['dis']
                post = Blogs(title=title, dis=dis)
                post.save()
                form = BlogForm()
        else:
            form = BlogForm()
        return render(request, 'add.html', {'form':form})
    else:
        return HttpResponseRedirect('/login')

def Update_blog(request, id):
    if request.user.is_authenticated:
        form = LoginForm()
        return render(request, 'update.html', {'form':form})
    else:
        return HttpResponseRedirect('/login')

def Delete_blog(request, id):
    if request.user.is_authenticated:
        form = SignUpForm()
        return render(request, 'dashboard.html', {'form':form})
    else:
        return HttpResponseRedirect('/login')