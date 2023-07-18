from django.contrib import admin
from django.urls import path,include
from .views import LandingView,SignUpView,LoginView,LogoutView

app_name='auths'

urlpatterns = [
    path('' , LandingView , name='landing'),
    path('login/' , LoginView , name='login'),
    path('signup/' , SignUpView , name='signup'),
    path('logout/' , LogoutView , name='logout'),
    path('homepage/' , include('pages.urls'))
]
