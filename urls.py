from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'login.views.login_view', name='login'),
    url(r'^citas/', include('cita.urls')),
    url(r'^plan_clases/', include('plan_clases.urls')),
    url(r'^lista_asistentes/', include('lista_asistentes.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
