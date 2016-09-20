from django.shortcuts import render
from django.http import HttpResponse

    
from .models import UserReview
from .models import CarReview
from review import models
import datetime

from django.http import JsonResponse
from django.contrib.auth import hashers
from django.forms.models import model_to_dict
from django import db


def index(request):
    return HttpResponse("Hello. You're at the reviews index.")

# Create your views here.
def create_CarReview(request):
    if request.method != POST:
        return _error_response(request, "must make POST request")
    if 'title' not in request.POST or       \
        'car_id' not in request.POST or     \
        'user_id' not in request.POST or    \
        'rating' not in request.POST or     \
        'text' not in request.POST:
        return _error_response(request, "missing required fields")

    c = models.UserReview(title=request.POST['title'], \
                           car_id=request.POST['car_id'], \
                            user_id = request.POST['user_id'],\
                           rating = request.POST['rating'], \
                           text = request.POST['text'], \
                           date = request.datetime.datetime.now() \
                           )

    try:
        u.save()
    except db.Error:
        return _error_response(request, "db error")

    return _success_response(request, {'title': c.pk})


def create_UserReview(request):
    if request.method != POST:
        return _error_response(request, "must make POST request")
    if 'title' not in request.POST or       \
        'user_id' not in request.POST or    \
        'text' not in request.POST:
        return _error_response(request, "missing required fields")

    ur = models.UserReview(title=request.POST['title'], \
                            user_id = request.POST['user_id'],\
                           text = request.POST['text'], \
                           date = request.datetime.datetime.now() \
                           )
    try:
        u.save()
    except db.Error:
        return _error_response(request, "db error")

    return _success_response(request, {'title': ur.pk})



#helper functions

def _error_response(request, error_msg):
    return JsonResponse({'ok': False, 'error': error_msg})

def _success_response(request, resp=None):
    if resp:
        return JsonResponse({'ok': True, 'resp': resp})
    else:
        return JsonResponse({'ok': True})
