from django.contrib import admin
from django.urls import path,include
from .views import display , ProfileView,searchView

app_name="pages"

urlpatterns = [
    path('' , display , name='display'),
    path('profile/' , ProfileView , name='profile'),
    path('search/', searchView , name='search')
]    

