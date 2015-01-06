from django.conf.urls import patterns,  url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('cita.views',
    # Examples:
    url(r'^$', 'cita', name='cita'),    
)
