from django.urls import path
from .views import *

urlpatterns = [
    path('index/', index, name='index'),  # Update this line to include 'index/'
    path('run_scraper/', run_scraper, name='run_scraper'), 
]
