"""
URL configuration for SchoolManagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path, include, re_path



from django.urls import path, include,re_path


from .views import *






urlpatterns = [

    path('about/' , about,name='about'),
    path('profile/' , profile,name='profile'),

    path('contact/' , contact,name='contact'),
    path('login/' , loginView,name='login'),
    path('register/' , Register,name='register'),
    path('logout/',logout_view,name='logout'),
    path('imuser/',selfuserdetails,name='selfdetails'),
    path('chat/',chatPage,name='chating'),
    path('myview/',my_view,name='my_view'),
    path('iamuser/<int:id>/', IamUserDetails.as_view(), name='iamuser'),
    path('userstat/<int:id>', UserActive_Inactive.as_view()),


    
    


]
