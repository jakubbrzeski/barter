from django.conf.urls import patterns, url

from barter import views

urlpatterns = patterns('',
   url(r'^$', views.login_user, name='login_user'),
)
