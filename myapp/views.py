from multiprocessing import context
from django.shortcuts import render
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


def counter(request):
    words = request.POST['words']
    total_words = len(words.split())
    return render(request, 'counter.html', {'amount': total_words})
