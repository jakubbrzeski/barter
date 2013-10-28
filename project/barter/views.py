from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse

from barter.models import *
from django.forms import ModelForm
import barter.authentication as A
def add(request):
   announcement = Announcement()
   announcement.author = request.user.username
   announcement.body = "I will exchange pig for a cow."
   return render_to_response('barter/add.html',{'announcement':announcement})
def log_out(request):
   A.log_out(request)
   return base(request)

def base(request):
   greeting = ""
   link = False
   if request.user.is_authenticated():
      link = True
      greeting = "Witaj " + request.user.username
   return render_to_response('barter/base.html',{'link':link,'greeting':greeting})
def register(request):
   user = A.addUser(request)
   if user is not None:
      return base(request)
   else:
      return render_to_response('barter/addUser.html')

def login_user(request):
   user = A.auth(request)
   if user is not None:
      return base(request)
 
   state = "Please log in below..."
   return render_to_response('barter/auth.html',{'state':state})   
