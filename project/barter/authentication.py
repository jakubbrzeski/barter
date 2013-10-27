from django.contrib.auth.models import User
from django.contrib.auth import authenticate

def addUser(request):
   username = request.POST.get('username')
   password = request.POST.get('password')
   email = request.POST.get('email')
   if username is None:
      return False
   user = User.objects.create_user(username,email,password)
   return True

def auth(request):
   if request.POST:
      name = request.POST.get('username')
      passw = request.POST.get('password')

      user = authenticate(username=name, password=passw)
      if user is not None:
	 if user.is_active:
	    return True
	 else:
            return False
      else:
	 return False
   else:
      return False
