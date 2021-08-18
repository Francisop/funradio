from django.shortcuts import render
from django.contrib.auth import authenticate
from sitePost.models import (AlbumsToLookoutFor,CollectionsToLookoutFor,LatestCollabs,NewMusicOnTheBlock,NewMusicTOLookoutFor,Song)
import json
# from django.http import HttpResponse

# Create your views here.


def index(request):
    collectionstolookoutfor = CollectionsToLookoutFor.objects.all()
    albumstolookoutfor = AlbumsToLookoutFor.objects.all()
    latestcollabs = LatestCollabs.objects.all()
    newmusicontheblock = NewMusicOnTheBlock.objects.all()
    newmusictolookoutfor = NewMusicTOLookoutFor.objects.all()
    song = Song.objects.all()
    

    if request.method == 'POST':
        method = request.POST.get('method')
        if method == 'login':
            print('login')
            email = request.POST.get('email-000')
            password = request.POST.get('password-000')
            user = authenticate(email = email,password = password)
            if user is not None:
                print(user)
            print('user doesnt exist')
        else:
            print('register')
            email = request.POST.get('email-000')
            password = request.POST.get('password-000')
            
    context = {
        "collectionstolookoutfor":collectionstolookoutfor,
        "albumstolookoutfor":albumstolookoutfor,
        "latestcollabs":latestcollabs,
        "newmusicontheblock":newmusicontheblock,
        "newmusictolookoutfor":newmusictolookoutfor,
        "song":song        
    }        
    return render(request, 'index.html', context)
