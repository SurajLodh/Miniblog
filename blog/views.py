from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
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
        return render(request, 'dashboard.html')
    else:
        return HttpResponseRedirect('/login')

def User_Logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def User_Signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulations !! You have become an Author.')
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
                user = authenticate(usernamme=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Login Successfully !!')
                    return HttpResponseRedirect('/dashboard')
                else:
                    messages.success(request, 'Opps something has gone wrong !!!')
                    return HttpResponseRedirect('/login')
        else:   
            form = LoginForm()
        return render(request, 'login.html', {'form':form})
    else:
        return HttpResponseRedirect('/dashboard')