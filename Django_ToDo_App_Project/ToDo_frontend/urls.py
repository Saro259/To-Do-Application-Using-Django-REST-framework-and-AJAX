from django.urls import path
from . import views

''' To render out the frontend template '''
urlpatterns = [
    path('', views.list, name="list"),
    
]