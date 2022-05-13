from multiprocessing import context
from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'name': 'Laxman',
        'age': 25,
        'sex': 'male',
        'country': 'Nepal'
    }
    return render(request, 'index.html', context)


def counter(request):
    words = request.GET['words']
    total_words = len(words.split())
    return render(request, 'counter.html', {'amount': total_words})
