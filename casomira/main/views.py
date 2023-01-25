from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Person, Aircraft, Flight
from django.shortcuts import redirect
from datetime import datetime, timezone, timedelta
from datetime import date
from .forms import FlightForm
import xlwt


def index(request):
    return render(request, "main/index.html")


def entry(request):
    person_list = Person.objects.order_by("id")
    aircraft_list = Aircraft.objects.order_by("id")
    context = {
        "person_list": person_list,
        "aircraft_list": aircraft_list,
    }

    if request.method == "POST":
        person_choosen = request.POST.getlist("person_choosen")
        aircraft_choosen = request.POST.getlist("aircraft_choosen")

        for person_ch in person_choosen:
            person = Person.objects.get(id=int(person_ch))
            person.active = "True"
            person.save()

        for aircraft_ch in aircraft_choosen:
            aircraft = Aircraft.objects.get(id=int(aircraft_ch))
            aircraft.active = "True"
            aircraft.save()
        return redirect("main:flights")

    return render(request, "main/entry.html", context)


def flights(request):

    flights_list = Flight.objects.order_by("takeoff")

    person_active_list = Person.objects.order_by("id").filter(active=True)
    aircraft_active_list = Aircraft.objects.order_by("id").filter(active=True)

    context = {
        "flights_list": flights_list,
        "person_active_list": person_active_list,
        "aircraft_active_list": aircraft_active_list,
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
        response = HttpResponse(content_type="application/ms-excel")
        response["Content-Disposition"] = 'attachment; filename="users.xls"'

        wb = xlwt.Workbook(encoding="utf-8")
        ws = wb.add_sheet("Flights")  # this will make a sheet named Flights

        # Sheet header, first row
        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = ["Takeoff", "Landing", "Zak", "Kapitan"]

        for col_num in range(len(columns)):
            ws.write(
                row_num, col_num, columns[col_num], font_style
            )  # at 0 row 0 column

        # Sheet body, remaining rows
        font_style = xlwt.XFStyle()

        rows = Flight.objects.all().values_list(
            "takeoff", "landing", "student_id", "captain_id"
        )
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, row[col_num], font_style)

        wb.save(response)
        return response
    return render(request, "main/end_day.html")
