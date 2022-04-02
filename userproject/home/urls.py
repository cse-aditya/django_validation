from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [

    path('', views.index, name="home="),                     #for blank path
    path('login', views.loginUser,name="login"),             #for login endpoint
    path('logout', views.logoutUser,name="logout"),          #for logout endpoint
]
