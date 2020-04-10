from django.urls import path

from . import views

app_name = 'tablica'
urlpatterns = [
    path('', views.ListaPostow.as_view(), name='post_lista'),
    path('dodaj', views.dodaj_post, name='post_dodaj'),
    path('usun.<int:pk>', views.UsunPost.as_view(), name='post_usun')
]
