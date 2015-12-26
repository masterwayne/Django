from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'login.views.login_page', name='login_page'),
    #url(r'^login/', include('login.urls')),
    url(r'^search/$', 'login.views.search'),
    url(r'^admin/', include(admin.site.urls)),
)
