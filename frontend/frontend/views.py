from django.http import HttpResponse
from django.shortcuts import render,redirect
from backend.models import electronics,gaming,movie,vehicles,products

# Homepage Render with object collectioons from database
def homepage(request):
    var1 = products.objects.all()
    dict1 = {
        "key": var1
    }
    return render(request, 'homepage.html',dict1)

# Thanking page after opinion is taken 
def thank(request):
    return render(request, 'thank.html')

# for categories inside of a homepage
def categories(request):
    var1 = products.objects.all()
    dict1 = {
        "key": var1
    }
    return render(request, 'category.html', dict1)

#man opinion page
def opinion(request):
    var =products.objects.all()
    dic = {
        "key": var
    }
    return render(request, 'opinion.html',dic)

# Functions to render info for each Category
def electronic(request):
    var = electronics.objects.all()
    dict1 = {
        'key' : var
    }
    return render(request, 'Electronics.html',dict1)

def vehicle(request):
    var = vehicles.objects.all()
    dic = {
        'key':var
    }
    return render(request, 'Vehicles.html', dic)

def game(request):
    var = gaming.objects.all()
    dic = {
        'key':var
    }
    return render(request, 'Games.html', dic)

def movies_to_show(request):
    var = movie.objects.all()
    dic = {
        'key':var
    }
    return render(request, 'Movies.html', dic)

