from django.urls import path

from . import views
from .views import lety

app_name = 'main'

urlpatterns = [
    path('', views.index, name='main'),
    path('zapis', views.zapis, name='zapis'), 
    path('lety', views.lety, name='lety'),
    path('ukoncene_lety', views.ukoncene_lety, name = 'ukoncene_lety'),

]