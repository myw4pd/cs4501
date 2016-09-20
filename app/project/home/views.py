from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse 

def index(request):
    return HttpResponse("Hello, world. You're at the home index.")
# Create your views here.
