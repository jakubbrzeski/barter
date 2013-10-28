from django.conf.urls import patterns, url

from barter import views

urlpatterns = patterns('',
   url(r'^$', views.base, name='base'),
   url(r'login', views.login_user, name='login_user'),
   url(r'register', views.register, name='register'),
   url(r'log_out', views.log_out, name='log_out'),
   url(r'add', views.add, name='add'),
)
