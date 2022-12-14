from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Person, Aircraft, Flight
from django import forms
from django.shortcuts import redirect
from datetime import datetime, timezone
from datetime import date


def index(request):
    return render(request, 'main/index.html')


def zapis(request):
    person_list = Person.objects.order_by('id')
    aircraft_list = Aircraft.objects.order_by('id')
    context = {
        'person_list': person_list,
        'aircraft_list' : aircraft_list,
    }


    if request.method == 'POST':
        person_choosen = request.POST.getlist('person_choosen')
        aircraft_choosen = request.POST.getlist('aircraft_choosen')


        for person_ch in person_choosen:
            person = Person.objects.get(id=int(person_ch))
            person.active = 'True'
            person.save()

        for aircraft_ch in aircraft_choosen:
            aircraft = Aircraft.objects.get(id=int(aircraft_ch))
            aircraft.active = 'True'
            aircraft.save()
        return redirect("main:lety")

    return render(request, 'main/zapis.html', context )


def lety(request):

    lety_list = Flight.objects.order_by('takeoff')

    person_active_list = Person.objects.order_by('id').filter(active=True)
    aircraft_active_list = Aircraft.objects.order_by('id').filter(active=True)

    context = {
        'lety_list': lety_list,
        'person_active_list': person_active_list,
        'aircraft_active_list': aircraft_active_list,
    }
    

    if request.method=="POST" and 'potvrdit_vzlet' in request.POST:
        aircraft=request.POST.get('aircraft')
        student=request.POST.get('student')
        capitan=request.POST.get('capitan')
        timestamp = datetime.now(timezone.utc)
        timestamp_date=datetime.today().date()
        new_flight = Flight(date=timestamp_date, aircraft_id=aircraft, captain_id=capitan, student_id=student, takeoff=timestamp)
        new_flight.save()
        
        aircraft_bow=request.POST.get('aircraft_bow')
        capitan_bow=request.POST.get('capitan_bow')
        if aircraft_bow == None:
            pass
        else:
            new_flight_bow = Flight(date=timestamp_date, aircraft_id=aircraft_bow, captain_id=capitan_bow, takeoff=timestamp)
            new_flight_bow.save()
        return redirect('main:lety')

    if request.method=="POST" and 'pristal' in request.POST:
        flight_to_end=request.POST.get('pristal')
        flight = Flight.objects.get(id=flight_to_end)
        timestamp1 = datetime.now(timezone.utc)
        flight.landing=timestamp1
        flight.save()

    return render(request, 'main/base.html', context)





def ukoncene_lety(request):
    lety_list = Flight.objects.order_by('id').exclude(landing__isnull = True)

    context = {
        'lety_list': lety_list,
    }
    print(lety_list)

    return render(request, 'main/base_ukoncene.html', context)



