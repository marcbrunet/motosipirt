# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import random
from datetime import datetime

from celery.task import periodic_task
from django.http.response import JsonResponse
from django.shortcuts import render
from models import lectura
from CanBus.ReadValues import readValues
from datetime import timedelta
inici = True
test = True
canBus = readValues()


@periodic_task(run_every=timedelta(seconds=1))
def ReadData():
    #data = {'RPM': random.randint(0, 8000), 'SOC': random.randint(0,100), 'Tbat': random.randint(0,200),
    #            'Tdriver': random.randint(0,200), 'Tengine': random.randint(0,100), 'Vbat':random.randint(0,100),
    #            'Imax': random.randint(0,500), 'Vmincell' : random.randint(0,420), 'Vmaxcell':random.randint(0,420),
    #            'Tmincell': random.randint(0,100),'Tmaxcell': random.randint(0,100)}

    global canBus
    data = canBus.canBusUpdater()

    lectura.objects.create(RPM=data['RPM'], SOC = data['SOC'], Tbat = data['Tbat'], Tdriver = data['Tdriver']
        , Tengine = data['Tengine'], Vbat = data['Vbat'], Imax = data['Imax'], Vmincell = data['Vmincell'], Vmaxcell = data['Vmaxcell'],
        Tmincell = data['Tmincell'], Tmaxcell = data['Tmaxcell']).save()

# Create your views here.

def index(request):
    values = {}
    batteryPercentage = 25
    rpm = datetime.now().second*100
    motorTemperature = 100
    speed = 210
    values['batteryPercentage'] = batteryPercentage
    values['rpm'] = rpm
    values['motorTemperature'] = motorTemperature
    values['speed'] = speed
    return render(request, 'display.html', values)

def refresh(request):
    values = {}
    batteryPercentage = 60
    rpm = 0
    motorTemperature = 30
    speed = 0
    values['batteryPercentage'] = batteryPercentage
    values['rpm'] = rpm
    values['motorTemperature'] = motorTemperature
    values['speed'] = speed
    return JsonResponse(values)