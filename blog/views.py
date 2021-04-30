from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, LoginForm, BlogForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Blogs
from django.contrib.auth.models import Group
# Create your views here.

def Home(request):
    posts = Blogs.objects.all()
    return render(request, 'home.html', {'posts':posts})

def About(request):

    return render(request, 'about.html')

def Contact(request):

    # messages.success(request, 'We will respond ASAP ...!!')
    return render(request, 'contact.html')

def Dashboard(request):
    if request.user.is_authenticated:
        posts = Blogs.objects.all()
        user = request.user
        full_name = user.get_full_name()
        gps = user.groups.all()
        return render(request, 'dashboard.html', {'posts':posts,'full_name':full_name, 'gps':gps})
    else:
        messages.success(request, 'Please login ...!!')
        return HttpResponseRedirect('/login')

def User_Logout(request):
    logout(request)
    messages.success(request, 'You have been successfully logged out ...!!')
    return HttpResponseRedirect('/')

def User_Signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='Author')
            user.groups.add(group)
            messages.success(request, 'Successfully Created Please login ...!!')
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
        messages.success(request, 'Already login ...!!')
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
                messages.success(request, 'Add Post Successfully ...!!')
                return HttpResponseRedirect('/dashboard')
        else:
            form = BlogForm()
        return render(request, 'add.html', {'form':form})
    else:
        messages.success(request, 'Please login ...!!')
        return HttpResponseRedirect('/login')

def Update_blog(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            obj = Blogs.objects.get(pk=id)
            form = BlogForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                messages.success(request, 'Updated Successfully ...!!')
                return HttpResponseRedirect('/dashboard')
        else:
            obj = Blogs.objects.get(pk=id)
            form = BlogForm(instance=obj)
        return render(request, 'update.html', {'form':form})
    else:
        messages.success(request, 'Please login ...!!')
        return HttpResponseRedirect('/login')

def Delete_blog(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            obj = Blogs.objects.get(pk=id)
            obj.delete()
            return HttpResponseRedirect('/dashboard')
        
        return render(request, 'dashboard.html', {'form':form})
    else:
        messages.success(request, 'Please login ...!!')
        return HttpResponseRedirect('/login')