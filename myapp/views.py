from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import *

# Create your views here.


def index1(request):
    context = {
        'name': 'Laxman',
        'age': 25,
        'sex': 'male',
        'country': 'Nepal'
    }
    return render(request, 'index1.html', context)


def index(request):
    features = Feature.objects.all()
    return render(request, 'index.html', {'features': features})


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        rpassword = request.POST['rpassword']

        if password == rpassword:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email alrady exists')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username alrady exists')
                return redirect('register')
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'register.html')


def counter(request):
    words = request.POST['words']
    total_words = len(words.split())
    return render(request, 'counter.html', {'amount': total_words})
