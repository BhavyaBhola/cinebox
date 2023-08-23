from django.shortcuts import render
import random
from django.contrib.auth.decorators import login_required
# Create your views here.
from .api import GetImages, PopularMoviesTitles,getDetails
from .models import Profile

@login_required
def display(request , *args , **kwargs):
    #titles = PopularMoviesTitles()
    user_profile = Profile.objects.get(user=request.user)

    context = {
        'user_profile':user_profile,
        "images":[],
        "titles":[],
        "details":[]
    }   

    #for i in range(len(titles)):
        #context["images"].append(GetImages(titles[i])['images'][0]['url'])
        #context['details'].append(getDetails(titles[i])['plotOutline']['text'])
        #context['titles'].append(getDetails(titles[i])['title']['title'])
    
    
    return render(request , 'pages/home.html' , context)

@login_required
def ProfileView(request , *args , **kwargs):
    user_profile = Profile.objects.get(user=request.user)

    if request.method=='POST':
        if request.FILES.get('image')==None:
            image = user_profile.profile_img   

            user_profile.profile_img=image   
            user_profile.save()

        if request.FILES.get('image')!=None:
            image = request.FILES.get('image')
            user_profile.profile_img = image
            user_profile.save()


    return render(request , 'pages/profile.html' , {'user_profile':user_profile})

@login_required
def searchView(request , *args , **kwargs):
    print(request)
    if request.method=='POST':
        movie_name = request.POST.get('search')
        #details = getDetails(movie_name)

        context = {
            'title':movie_name
        }

        return render(request , 'pages/search_page.html' , context)