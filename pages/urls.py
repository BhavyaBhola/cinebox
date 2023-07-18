from django.contrib import admin
from django.urls import path,include
from .views import display , ProfileView

app_name="pages"

urlpatterns = [
    path('' , display , name='display'),
    path('profile/' , ProfileView , name='profile')
]    

