from django.shortcuts import render

#from django.http import JsonResponse
from django.contrib.auth import hashers
from django.forms.models import model_to_dict
from django import db
from django.http import HttpResponse

from main import models

# APIs for accessing Users

def index(request):
    return HttpResponse("Hello. You're at the main index.")

def create_user(request):
    if request.method != 'POST':
        return _error_response(request, "must make POST request")
    if 'first_name' not in request.POST or     \
       'last_name' not in request.POST or     \
       'password' not in request.POST or   \
       'username' not in request.POST:
        return _error_response(request, "missing required fields")

    u = models.User(username=request.POST['username'],                         \
                    first_name=request.POST['first_name'],                             \
                    last_name=request.POST['last_name'],                             \
                    password=hashers.make_password(request.POST['password']),  \
                   date_joined=datetime.datetime.now()                        \
                    )

    try:
        u.save()
    except db.Error:
        return _error_response(request, "db error")

    return _success_response(request, {'user_id': u.pk})
#Get user
def lookup_user(request, user_id):
    if request.method != 'GET':
        return _error_response(request, "must make GET request")

    try:
        u = models.User.objects.get(pk=user_id)
    except models.User.DoesNotExist:
        return _error_response(request, "user not found")

    return _success_response(request, {'username': u.username,      \
                                       'first_name': u.first_name,          \
                                       'last_name': u.last_name,          \
                                       'date_joined': u.date_joined \
                                    #   'location': u.location \
                                       })

def update_user(request, user_id):
    if request.method != 'POST':
        return _error_response(request, "must make POST request")

    try:
        u = models.User.objects.get(pk=user_id)
    except models.User.DoesNotExist:
        return _error_response(request, "user not found")

    changed = False
    if 'first_name' in request.POST:
        u.first_name = request.POST['first_name']
        changed = True
    if 'last_name' in request.POST:
        u.l_name = request.POST['last_name']
        changed = True
    if 'password' in request.POST:
        u.password = hashers.make_password(request.POST['password'])
        changed = True

    if not changed:
        return _error_response(request, "no fields updated")

    u.save()

    return _success_response(request)
# Create your views here.
