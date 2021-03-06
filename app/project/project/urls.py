"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
from main import views as main_views
from review import views as review_views

urlpatterns = patterns('',
    url(r'^review/', include('review.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', include('main.urls')),
    url(r'^api/v1/users/create$', main_views.create_user),
    url(r'^api/v1/users/(\d+)$', main_views.lookup_user),
    url(r'^api/v1/users/(\d+)/update$', main_views.update_user),
    url(r'^api/v1/review/create$', review_views.create_UserReview),
    url(r'^api/v1/review/(\d+)$', review_views.lookup_userReview),

)