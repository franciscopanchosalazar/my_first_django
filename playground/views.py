from django.shortcuts import render
from django.http import HttpResponse    # Imported to be able to handle requests  


# Create your views here.

def say_hello(request):
    # return render(request, 'my_template.html')
    return HttpResponse('Keep learning :)')


# This is the way to call an html file
# Do not forget to map this request so whenever we request that url it will call the view (urls.py)
def my_home(request):
    return render(request, 'my_template.html')
