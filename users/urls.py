from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
    path('rejestruj/', views.rejestruj, name='rejestruj'),
    path('loguj/', views.loguj, name='loguj'),
    path('wyloguj/', views.wyloguj, name='wyloguj'),
]
