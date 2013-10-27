from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse

from barter.models import *
from django.forms import ModelForm
import barter.authentication as A
def add(request):
   announcement = Announcement()
   announcement.author = "Guest"
   announcement.body = "I will exchange pig for a cow."
   return render_to_response('barter/add.html',{'announcement':announcement})
def base(request):
    return render_to_response('barter/base.html')
def hello(request):
   return HttpResponse("Hello World!")
def register(request):
   if A.addUser(request) is True:
      return render_to_response('barter/base.html')
   else:
      return render_to_response('barter/addUser.html')

def login_user(request):
   if A.auth(request) is True:
      return HttpResponse("OK!")
 
   state = "Please log in below..."
   return render_to_response('barter/auth.html',{'state':state})   
