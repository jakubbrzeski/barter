from django.conf.urls import patterns, url

from barter import views

urlpatterns = patterns('',
   url(r'^$', views.index, name='index'),
   url(r'login', views.login_user, name='login_user'),
   url(r'hello', views.hello, name='hello_world'),
   
)
