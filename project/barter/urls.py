from django.conf.urls import patterns, url

from barter import views

urlpatterns = patterns('',
   url(r'^$', views.base, name='base'),
   url(r'login', views.login_user, name='login_user'),
   url(r'hello', views.hello, name='hello_world'),
   url(r'register', views.register, name='register'),
   url(r'add', views.add, name='add'),
)
