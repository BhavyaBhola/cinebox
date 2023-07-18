from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib import messages
from pages.models import Profile
# Create your views here.

# Create your views here.

def LandingView(request , *args , **kwargs):

    if request.user.is_anonymous:
        return redirect('login/')

    return redirect('homepage/')#return render(request , 'pages/home.html')

def SignUpView(request , *args , **kwargs):
    if request.method == 'POST':
        username = request.POST.get('username')
        p1 = request.POST.get('password1')
        p2 = request.POST.get('password2')

        if p1 == p2:
            if User.objects.filter(username=username).exists():
                messages.info(request , 'username already exists')
                return redirect("/signup")
            else:
                user = User.objects.create_user(username=username , password=p1)
                user.save()

                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model)
                new_profile.save()
                return redirect('/login')
        else:
            messages.info(request , 'passwords does not match')
            return redirect('/signup')    
        
    return render(request , 'authi/signup.html')    

def LoginView(request , *args , **kwargs):
    
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username , password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.info(request , 'wrong credentials')
            return render(request , 'authi/login.html') 
        
    return render(request , 'authi/login.html')   

def LogoutView(request , *args , **kwargs):
    logout(request)
    return redirect(reverse("auths:landing"))