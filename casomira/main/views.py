from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, FileResponse
from main.models import Person, Aircraft, Flight
from django.shortcuts import redirect
from datetime import datetime, timezone, timedelta
from datetime import date
from .forms import FlightForm
import csv

def index(request):
    return render(request, "main/index.html")


def entry(request):
    #check if there is no valid entry yet
    #request only the needed values .values('active', 'name', 'id')
    people_active = Person.objects.values_list("active").filter(active = True)
    aircrafts_active = Aircraft.objects.values_list("active").filter(active = True)

    if people_active or aircrafts_active:
        return HttpResponseRedirect("flights")

    person_list = Person.objects.values("id", "first_name", "last_name").order_by("id")
    aircraft_list = Aircraft.objects.values("id", "registration").order_by("id")

    context = {
        "person_list": person_list,
        "aircraft_list": aircraft_list,
    }

    if request.method == "POST":
        person_choosen = request.POST.getlist("person_choosen")
        aircraft_choosen = request.POST.getlist("aircraft_choosen")

    #Person.object.filter(id__in=person_list).update(active=True)
        Person.objects.filter(id__in=person_choosen).update(active=True)
        Aircraft.objects.filter(id__in=aircraft_choosen).update(active=True)

        return redirect("main:flights")

    return render(request, "main/entry.html", context)


def flights(request):

    #Check if there is an active running entry, if not, redirect to the start entry page
    people_active_count = Person.objects.values_list("active").filter(active = True).count()
    aircrafts_active_count = Aircraft.objects.values_list("active").filter(active = True).count()
    if people_active_count == 0 or aircrafts_active_count == 0:
        return HttpResponseRedirect("entry")


    flights_list_landed = Flight.objects.filter(landing__isnull = False).order_by("takeoff")
    flights_list_not_landed = Flight.objects.filter(landing__isnull = True).order_by("takeoff")

    person_active_list = Person.objects.order_by("id").filter(active=True, in_the_sky=False)
    aircraft_active_list = Aircraft.objects.order_by("id").filter(active=True, in_the_sky=False)


    context = {
        "flights_list": flights_list_landed,
        "person_active_list": person_active_list,
        "aircraft_active_list": aircraft_active_list,
        "flights_not_landed":  flights_list_not_landed,
    }

    if request.method == "POST" and "confirm_takeoff" in request.POST:

        Flight(
            aircraft_id=request.POST.get("aircraft"),
            captain_id=request.POST.get("capitan"),
            student_id=request.POST.get("student"),
            takeoff=datetime.now(timezone.utc),
        ).save()
        Person.objects.filter(id=request.POST.get("capitan")).update(in_the_sky=True)
        Person.objects.filter(id=request.POST.get("student")).update(in_the_sky=True)
        Aircraft.objects.filter(id=request.POST.get("aircraft")).update(in_the_sky=True)

        if request.POST.get("aircraft_bow") == None:
            pass
        else:
            Flight(
                aircraft_id=request.POST.get("aircraft_bow"),
                captain_id= request.POST.get("capitan_bow"),
                takeoff=datetime.now(timezone.utc)
            ).save()
            Person.objects.filter(id=request.POST.get("capitan")).update(in_the_sky=True)
            Person.objects.filter(id=request.POST.get("student")).update(in_the_sky=True)
            Aircraft.objects.filter(id=request.POST.get("aircraft")).update(in_the_sky=True)

        return redirect("main:flights")

    if request.method == "POST" and "landed" in request.POST:
        flight = Flight.objects.get(id= request.POST.get("landed"))
        flight.landing = datetime.now(timezone.utc)
        flight.save()
        Person.objects.filter(id=flight.captain.id).update(in_the_sky=False)
        Person.objects.filter(id=flight.student.id).update(in_the_sky=False)
        Aircraft.objects.filter(id=flight.aircraft.id).update(in_the_sky=False)


    return render(request, "main/base.html", context)


def finished_flights(request):
    flights_list = Flight.objects.filter(landing__isnull = False, date = date.today()).order_by("-takeoff")

    context = {
        "flights_list": flights_list,
    }

    return render(request, "main/base_finished_flights.html", context)


def finished_flights_update(request, id):
    flight = Flight.objects.get(id=id)
    form = FlightForm(instance=flight)
    # flights_list = Flight.objects.order_by("id").exclude(landing__isnull=True)
    context = {
        "form": form,
        # "flights_list": flights_list,
    }

    if request.method == "POST":
        form = FlightForm(request.POST, instance=flight)
        if form.is_valid():
            form.save()
            return redirect("main:finished_flights")
    else:
        form = FlightForm(instance=flight)

    return render(request, "main/finished_flights_edit.html", context)


def end_day(request):

    flights_not_landed = Flight.objects.filter(landing__isnull = True)
    if request.method == "POST" and "ukoncit" in request.POST:
        #first we ckeck if all the flights are finished

        if flights_not_landed:
            print("You can't finish the day, there are still some aircrafts in the sky")
            messages.add_message(request, messages.WARNING, 'Nope. There are still some aircrafts in the sky.')

        else:
            #if all the flights are finished we deactivate people and aircrafts
            Person.objects.filter(active = True).update(active = False)
            Aircraft.objects.filter(active = True).update(active = False)
            return redirect("/main/")

    if request.method == "POST" and "stahnout" in request.POST:
        if flights_not_landed:
            messages.add_message(request, messages.WARNING, 'Nope. There are still some aircrafts in the sky.')
        else:
            todays_flights = Flight.objects.filter(date = date.today())
            response = HttpResponse(
                content_type='text/csv',
                headers={'Content-Disposition': f'attachment; filename="provoz_{date.today()}.csv"'},
            )
            writer = csv.writer(response, delimiter=',', dialect='excel')
            writer.writerow(["Datum", "Student", "Kapitan", "Letadlo", "Odlet", "Pristnani", "Delka"])
            for f in todays_flights:
                writer.writerow([f.date, f.student, f.captain, f.aircraft, f.takeoff, f.landing, f.duration ])
            return response
            #and we create a csv file based on the flights
    return render(request, "main/end_day.html")



#Additional funcsions

# def csv_end_day(flights):
#     with open ('first.csv', 'w', newline="") as csvfile:
#         writer = csv.writer(csvfile, delimiter=',', dialect='excel')
#         writer.writerow(["Datum", "Student", "Kapitan", "Letadlo", "Odlet", "Pristnani", "Delka"])
#         for f in flights:
#             writer.writerow([f.date, f.student, f.captain, f.aircraft, f.takeoff, f.landing, f.duration ])
#     return csvfile