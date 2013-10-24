from django.conf.urls import patterns, include, url

fron django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
   url(r'barter/', include('barter.urls')),
   url(r'admin/', include(admin.site.urls)),
)
