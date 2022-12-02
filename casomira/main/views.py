from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Person, Aircraft, Flight
from django import forms
from django.shortcuts import redirect
from datetime import date
import datetime

# from django.utils.timezone import datetime
# Create your views here.

def index(request):
    return render(request, 'main/index.html')


def zapis(request):
    person_list = Person.objects.order_by('id')
    aircraft_list = Aircraft.objects.order_by('id')
    context = {
        'person_list': person_list,
        'aircraft_list' : aircraft_list,
    }

    print(person_list)


    if request.method == 'POST':
        person_choosen = request.POST.getlist('person_choosen')
        aircraft_choosen = request.POST.getlist('aircraft_choosen')


        if len(person_choosen)<2 or len(aircraft_choosen)<1:
            pass
        else:
            for person_ch in person_choosen:
                person = Person.objects.get(id=int(person_ch))
                person.active = 'True'
                person.save()

            for aircraft_ch in aircraft_choosen:
                aircraft = Aircraft.objects.get(id=int(aircraft_ch))
                aircraft.active = 'True'
                aircraft.save()
            return HttpResponseRedirect('lety')

    return render(request, 'main/zapis.html', context )


def lety(request):
    # today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
    # today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)
    # flight_list = Flight.objects.filter(date__range=(today_min, today_max))
    # print(flight_list)
    lety_list = Flight.objects.order_by('takeoff')
    context = {
        'lety_list': lety_list,
    }
    # print(lety_list)
    return render(request, 'main/base.html', context)



def ukoncene_lety(request):
    return render(request, 'main/base_ukoncene.html')



