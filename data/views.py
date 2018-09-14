# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import random
from datetime import datetime
from django.http.response import JsonResponse
from django.shortcuts import render

from models import lectura


def addData(data):
    datafield = lectura(RPM=data['RPM'], SOC=data['SOC'], Tbat=data['Tbat'],
                        Tdriver= data['Tdriver'], Tengine=data['Tengine'],
                        Vbat= data['Vbat'], Imax = data['Imax'],
                        Vmincell = data['Vmincell'], Vmaxcell=data['Vmaxcell'], Tmincell=['Tmincell'],
                        Tmaxcell=data['Tmaxcell'])
    datafield.save()

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

def lectura(request):
    return index(request)

def refresh(request):
    values = {}
    batteryPercentage = 100 - int((datetime.now().second*100/60))
    rpm = datetime.now().microsecond*6000/1000000
    motorTemperature = 100 + random.randint(-10,10)
    speed = random.randint(0, 201)
    values['batteryPercentage'] = batteryPercentage
    values['rpm'] = rpm
    values['motorTemperature'] = motorTemperature
    values['speed'] = speed
    return JsonResponse(values)