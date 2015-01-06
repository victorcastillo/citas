from django.conf.urls import patterns,  url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('plan_clases.views',
    # Examples:
    url(r'^$', 'plan_clases', name='plan_clases'),
)
