from django.conf.urls import *
from django.contrib import admin
 
admin.autodiscover()
 
urlpatterns = patterns('',
    (r'^admin/(.*)', admin.site), #Lets us access the admin page
    (r'^$', 'Todo.views.index'), #Our index page, it maps to / . Once the page is called it will look in /todo/core/views.py for a function called index
     
)
