from django.urls import path
from .views import *

app_name = 'users'
urlpatterns = [
    path('sign-up', SignUp.as_view(), name='sign_up'),
    path('sign-in', SignIn.as_view(), name='sign_in'),
    path('profile/<int:pk>/', Profile.as_view(), name='profile'),
    path('sign-out/', SignOut.as_view(), name='sign_out'),
]
