from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from main.models import Person, Aircraft, Flight
from django.shortcuts import redirect
from datetime import datetime, timezone, timedelta
from datetime import date
from .forms import FlightForm
import csv

def index(request):
    return render(request, "main/index.html")


def entry(request):
    #request only the needed values .values('active', 'name', 'id')
    person_list = Person.objects.order_by("id")
    aircraft_list = Aircraft.objects.order_by("id")
    #[a for a in aircraft_list if a.active]
    #check if there is no valid entry yet 
    people_active = Person.objects.filter(active=True).exists()
    aircrafts_active = Aircraft.objects.filter(active=True).exists()
    #.values('active', 'name')
    #count()
    if people_active or aircrafts_active:
        return HttpResponseRedirect("flights")


    
    context = {
        "person_list": person_list,
        "aircraft_list": aircraft_list,
    }

    if request.method == "POST":
        person_choosen = request.POST.getlist("person_choosen")
        aircraft_choosen = request.POST.getlist("aircraft_choosen")

    #Person.object.filter(id__in=person_list).update(active=True)
        for person_ch in person_choosen:
            person = Person.objects.get(id=int(person_ch))
            person.active = True
            person.save()

        for aircraft_ch in aircraft_choosen:
            aircraft = Aircraft.objects.get(id=int(aircraft_ch))
            aircraft.active = True
            aircraft.save()
        return redirect("main:flights")

    return render(request, "main/entry.html", context)


def flights(request):
    #Check if there is an active running entry, if not, redirect to the start entry page 
    people_active = Person.objects.filter(active=True)
    aircrafts_active = Aircraft.objects.filter(active=True)
    if len(people_active) == 0 or len(aircrafts_active) == 0:
        return HttpResponseRedirect("entry")


    flights_list = Flight.objects.order_by("takeoff")
    flights_not_landed = Flight.objects.filter(landing__isnull = True)

    person_active_list = Person.objects.order_by("id").filter(active=True)
    aircraft_active_list = Aircraft.objects.order_by("id").filter(active=True)

    context = {
        "flights_list": flights_list,
        "person_active_list": person_active_list,
        "aircraft_active_list": aircraft_active_list,
        "flights_not_landed": flights_not_landed,
    }

    if request.method == "POST" and "confirm_takeoff" in request.POST:
        aircraft = request.POST.get("aircraft")
        student = request.POST.get("student")
        capitan = request.POST.get("capitan")
        timestamp = datetime.now(timezone.utc)
        # timestamp_date=datetime.today().date()
        new_flight = Flight(
            aircraft_id=aircraft,
            captain_id=capitan,
            student_id=student,
            takeoff=timestamp,
        )
        new_flight.save()

        aircraft_bow = request.POST.get("aircraft_bow")
        capitan_bow = request.POST.get("capitan_bow")
        if aircraft_bow == None:
            pass
        else:
            new_flight_bow = Flight(
                aircraft_id=aircraft_bow, captain_id=capitan_bow, takeoff=timestamp
            )
            new_flight_bow.save()
        return redirect("main:flights")

    if request.method == "POST" and "landed" in request.POST:
        flight_to_end = request.POST.get("landed")
        flight = Flight.objects.get(id=flight_to_end)
        timestamp1 = datetime.now(timezone.utc)
        flight.landing = timestamp1
        flight.save()

    return render(request, "main/base.html", context)


def finished_flights(request):
    flights_list = Flight.objects.order_by("-takeoff").exclude(landing__isnull=True)

    context = {
        "flights_list": flights_list,
    }

    return render(request, "main/base_finished_flights.html", context)


def finished_flights_update(request, id):
    flight = Flight.objects.get(id=id)
    form = FlightForm(instance=flight)
    flights_list = Flight.objects.order_by("id").exclude(landing__isnull=True)
    context = {
        "form": form,
        "flights_list": flights_list,
    }

    if request.method == "POST":
        form = FlightForm(request.POST, instance=flight)
        if form.is_valid():
            # update the existing `Band` in the database
            form.save()
            # redirect to the detail page of the `Band` we just updated
            return redirect("main:finished_flights")
    else:
        form = FlightForm(instance=flight)

    return render(request, "main/finished_flights_edit.html", context)


def end_day(request):
    if request.method == "POST":
        #first we ckeck if all the flights are finished
        flights_not_landed = Flight.objects.filter(landing__isnull = True)
        if flights_not_landed:
            print("You can't finish the day, there are still some aircrafts in the sky")
        else:
            #if all the flights are finished we deactivate people and aircrafts
            people = Person.objects.all()
            aircrafts = Aircraft.objects.all()
            for p in people:
                p.active = "False"
                p.save()
            for a in aircrafts:
                a.active = "False"
                a.save()
            return redirect("/main/")
            #and we create a csv file based on the flights
    return render(request, "main/end_day.html")


#Additional funcsions

def csv_end_day():
    pass
