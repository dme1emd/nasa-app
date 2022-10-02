from django.shortcuts import render , redirect
from profiles.models import Profile
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
def home(request) : 
    return render(request,'home.html' , context={'user' : request.user})
def market(request) : 
    return render(request,'market.html' , context={'user' : request.user})
def index(request) : 
    return render(request,'index.html' , context={'user' : request.user})
def quiz(request) : 
    return render(request,'az.html' , context={'user' : request.user})
def cart(request) : 
    return render(request,'cart.html' , context={'user' : request.user})
def travel(request) : 
    return render(request,'travel.html' , context={'user' : request.user})
def signin(request) : 
    if request.method == 'POST' : 
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email)
        try : 
            user = Profile.objects.get(email = email)
            if user.check_password(password):
                login(request , user)
                return redirect('/home/')
            else:
                messages.error(request,'creadentials not matching')
        except : 
            messages.error(request , 'there is no account with this email')
    return render(request,'signin.html' , context={'user' : request.user})
def signup(request) : 
    email = request.GET.get('email') 
    password = request.GET.get('password')
    username = request.GET.get('username')
    profile = Profile.objects.filter(email = email)
    if email :
        if not profile :
            profile = Profile.objects.create(email = email , username = username)
            profile.set_password(password)
            profile.save()
        else : 
            messages.error(request , 'a profile with this email already exists')
    return render(request,'signup.html' , context={'user' : request.user})
def mars(request) : 
    return render(request,'mars.html' , context={'user' : request.user})
def logout_view(request) : 
    logout(request)
    return redirect('signin')
def profile(request) : 
    return render(request,'profile.html' , context={'request' : request})