from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.hashers import make_password
from sitePost.models import (LatestAlbums, EventsInTheCity, NewMusicOnTheBlock,Song)
from django.contrib.auth import get_user_model
import json
# from django.http import HttpResponse

# Create your views here.

User = get_user_model()


def index(request):
    latestalbums = LatestAlbums.objects.all()
    newmusicontheblock = NewMusicOnTheBlock.objects.all()
    eventsinthecity = EventsInTheCity.objects.all()
    song = Song.randomise.random()
    currentUser = False
    
   
    if (request.user.is_authenticated ):
        print(request.user)
        currentUser = True        
    else:
        print(request.user)
        currentUser = False 
        print('you need to login')
    

    if request.method == 'POST':
        method = request.POST.get('method')
        if method == 'login':
            print('login')
            email = request.POST.get('email-000')
            password = request.POST.get('password-000')
            user = authenticate(request,email = email,password = password)
            if user is not None:
                print('user is real')
                login(request,user)
                currentUser = True
                context = {     
                            "eventsinthecity":eventsinthecity,
                            "latestalbums":latestalbums,
                            "newmusicontheblock":newmusicontheblock,
                            "song":song,    
                            "currentUser":currentUser,
                        }
                return render(request, 'index.html', context)
            else:
                print("user doesn't exist")
                context = {}
                return render(request, 'index.html', context)
        elif method == 'register':
            print('register')
            # fullname = request.POST.get('name-000')
            email = request.POST.get('email-000')
            password = request.POST.get('password-000')
            user = User.objects.create(email = email,password = make_password(password))
            user.save()
            context = {
                            "eventsinthecity":eventsinthecity,
                            "latestalbums":latestalbums,
                            "newmusicontheblock":newmusicontheblock,
                    "song":song,    
                    "currentUser":currentUser,
                            
            }
            return render(request, 'index.html', context)
            
        else:
            logout(request)
            currentUser = False
            context = {
                "song":song,    
                "currentUser":currentUser,
                }
            return render(request, 'index.html', context)
               
    context = {
                            "eventsinthecity":eventsinthecity,
                            "latestalbums":latestalbums,
                            "newmusicontheblock":newmusicontheblock,
        "song":song,    
        "currentUser":currentUser,
    }  
    return render(request, 'index.html', context)
