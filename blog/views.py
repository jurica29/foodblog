from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

import requests

# Create your views here.

#4f3bfbf8
#3ae08ae7be7d3cec4d482eba3cc36dc8


def index(request):
    query = "food"
    response = requests.get("https://api.edamam.com/api/recipes/v2?type=public&q="+query+"&app_id=4f3bfbf8&app_key=3ae08ae7be7d3cec4d482eba3cc36dc8")
    jsonResponse = response.json()
    recipes = jsonResponse['hits']
    return render(request,"blog/index.html", {'recipes':recipes})

def specific(request):
    return HttpResponse("This is the specific url")

def search(request):
    if request.method == "POST":
        userText = request.POST.get('userText')
        response = requests.get("https://api.edamam.com/api/recipes/v2?type=public&q="+userText+"&app_id=4f3bfbf8&app_key=3ae08ae7be7d3cec4d482eba3cc36dc8")
        jsonResponse = response.json()
        recipes = jsonResponse['hits']
        return render(request,"blog/index.html",{'recipes': recipes})    
    else: 
        return render(request, "blog/index.html")

def articles(request):
    return render(request,'blog/articles.html')

def contact(request):
    return render(request,'blog/contact.html')
