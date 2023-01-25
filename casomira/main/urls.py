from django.urls import path

from . import views
from .views import flights

app_name = "main"

urlpatterns = [
    path("", views.index, name="main"),
    path("entry", views.entry, name="entry"),
    path("flights", views.flights, name="flights"),
    path("finished_flights", views.finished_flights, name="finished_flights"),
    path("flights/<int:id>/edit", views.finished_flights_update, name="edit"),
    path("end_day", views.end_day, name="end_day"),
]
