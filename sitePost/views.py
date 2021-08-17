from django.shortcuts import render
from django.contrib.auth import authenticate

import json
# from django.http import HttpResponse

# Create your views here.


def index(request):
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
        
    return render(request, 'index.html', {})
