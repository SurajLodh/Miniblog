from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.Home),
    path('about/', views.About, name='about'),
    path('contact/', views.Contact, name='contact'),
    path('dashboard/', views.Dashboard, name='dashboard'),
    path('logout/', views.User_Logout, name='logout'),
    path('signup/', views.User_Signup, name='signup'),
    path('login/', views.User_Login, name='login'),
    path('addpost/', views.Add_blog, name='addpost'),
    path('update/<int:id>/', views.Update_blog, name='update'),
    path('delete/<int:id>/', views.Delete_blog, name='delete'),
]