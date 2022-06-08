from django.shortcuts import render
from django.http import HttpResponse

import requests

# Create your views here.

#4f3bfbf8
#3ae08ae7be7d3cec4d482eba3cc36dc8


def index(request):
    query = "cheese"
    response = requests.get("https://api.edamam.com/api/recipes/v2?type=public&q="+query+"&app_id=4f3bfbf8&app_key=3ae08ae7be7d3cec4d482eba3cc36dc8")
    return render(request,"blog/index.html")

def specific(request):
    return HttpResponse("This is the specific url")

