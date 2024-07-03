from django.urls import path
from . import views

# Here we map our urls to our views, eg. if we have "playground/hello/" in our browser, it will show
# any content inside the say_hello function (located in views.py) 
urlpatterns = [
    path('hello/', views.say_hello),
    path('my_home/', views.my_home),

]