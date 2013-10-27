from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse

from barter.models import *
from django.forms import ModelForm

def add(request):
   announcement = Announcement()
   announcement.author = "Guest"
   announcement.body = "I will exchange pig for a cow."
   return render_to_response('barter/add.html',{'announcement':announcement})
def base(request):
    return render_to_response('barter/base.html')
def hello(request):
   return HttpResponse("Hello World!")
def login_user(request):
   state = "Please log in below..."
   username = password = ''
   if request.POST:
      username = request.POST.get('username')
      password = request.POST.get('password')

      user = authenticate(username=username, password=password)
      if user is not None:
	 if user.is_active:
	    login(request,user)
	    state="You're logged in"
	 else:
	    state = "not active"
      else:
	 state = "Incorrect";
   return render_to_response('barter/auth.html',{'state':state, 'username': username})
