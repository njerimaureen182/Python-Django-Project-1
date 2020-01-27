# this function maps out the url to the view function
from django.urls import path

# to import the views module to the urls module:
# the '.' represents the current folder
from . import views


urlpatterns = [
    # the path function contains an empty string that specifies our url endpoint
    # tip: when we import a module, that module ends up being an object so we can use the dot operator to access
    # functions from that module
    path('', views.index),
    path('new', views.new)
]

