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
    feature1 = Feature()
    feature1.id = 0
    feature1.name = 'Laxman Maharjan'
    feature1.details = 'I am a programmer'
    feature1.is_true = True

    feature2 = Feature()
    feature2.id = 1
    feature2.name = 'Anita Maharjan'
    feature2.details = 'I am a nurse'
    feature2.is_true = False

    features = [feature1, feature2]
    return render(request, 'index.html', {'features': features})


def counter(request):
    words = request.POST['words']
    total_words = len(words.split())
    return render(request, 'counter.html', {'amount': total_words})
