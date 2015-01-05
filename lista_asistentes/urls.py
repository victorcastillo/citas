from django.conf.urls.defaults import patterns,  url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('lista_asistentes.views',
    # Examples:
    url(r'^$', 'lista_asistentes', name='lista_asistentes'),
)
