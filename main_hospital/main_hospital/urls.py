"""main_hospital URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()
urlpatterns = [
    url(r'^$','Accounts.views.home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$','main_hospital.views.login'),
    url(r'^logout/$','main_hospital.views.logout'),
    url(r'^auth/$','main_hospital.views.auth_view'),
    url(r'^loggedin/$','main_hospital.views.loggedin'),
    url(r'^invalid/$','main_hospital.views.invalid_login'),
    url(r'^register/$','main_hospital.views.register_user'),
    url(r'^register_success/$','main_hospital.views.register_success'),
]
