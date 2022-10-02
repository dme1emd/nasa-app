from django.urls import path
from .views import *
urlpatterns = [
    path('home/' , home),
    path('market/' , market),
    path('quiz/' , quiz),
    path('cart/' , cart),
    path('travel/' , travel),
    path('signin/' , signin , name = 'signin'),
    path('signup/' , signup),
    path('mars/' , mars),
    path('logout/' , logout_view),
    path('profile/' , profile),
]