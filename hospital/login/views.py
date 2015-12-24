from django.http import HttpResponse
from django.shortcuts import render

def login_page(request):
    return render(request, 'login_page.html')

def search(request):
    if 'username' in request.POST:
        message = 'You searched for: %r' % request.POST['username']
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)
