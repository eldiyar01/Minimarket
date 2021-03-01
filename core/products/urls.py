from django.urls import path, include
from .views import *

app_name = 'products'
urlpatterns = [
    path('', home, name='home'),
]
