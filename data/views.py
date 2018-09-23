# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import random
from datetime import datetime

#from celery.schedules import crontab
#from celery.task import periodic_task
from django.http.response import JsonResponse
from django.shortcuts import render
#from models import lectura
from CanBus.ReadValues import readValues
from datetime import timedelta
inici = True
test = True
canBus = readValues()


#@periodic_task(run_every=timedelta(seconds=1))
def ReadData():
    data = {'RPM': random.randint(0, 8000), 'SOC': random.randint(0,100), 'Tbat': random.randint(0,200),
                'Tdriver': random.randint(0,200), 'Tengine': random.randint(0,100), 'Vbat':random.randint(0,100),
                'Imax': random.randint(0,500), 'Vmincell' : random.randint(0,420), 'Vmaxcell':random.randint(0,420),
                'Tmincell': random.randint(0,100),'Tmaxcell': random.randint(0,100)}

    #global canBus
    #data = canBus.canBusUpdater()

    lectura.objects.create(RPM=data['RPM'], SOC = data['SOC'], Tbat = data['Tbat'], Tdriver = data['Tdriver']
        , Tengine = data['Tengine'], Vbat = data['Vbat'], Imax = data['Imax'], Vmincell = data['Vmincell'], Vmaxcell = data['Vmaxcell'],
        Tmincell = data['Tmincell'], Tmaxcell = data['Tmaxcell']).save()

# Create your views here.

def index(request):
    values = {}
    values['RPM'] = random.randint(0, 8000)
    values['Imax'] = random.randint(0, 200)
    values['Vbat'] = random.randint(0, 200)
    values['SOC'] = random.randint(0, 100)
    values['SOC_LV'] = random.randint(0, 100)
    values['Vmincell'] = random.randint(0, 200)
    values['Vmaxcell'] = random.randint(0, 200)
    values['Tmincell'] = random.randint(0, 200)
    values['Tmaxcell'] = random.randint(0, 200)
    values['Tbat'] = random.randint(0, 200)
    values['Tbat_LV'] = random.randint(0, 200)
    values['Tengine'] = random.randint(0, 200)
    values['Tdriver'] = random.randint(0, 200)
    values['Speed'] = random.randint(0, 200)
    return render(request, 'new_display.html', values)

def refresh(request):
    values = {}
    values['RPM'] = random.randint(0, 8000)
    values['Imax'] = random.randint(0, 200)
    values['Vbat'] = random.randint(0, 200)
    values['SOC'] = random.randint(0, 100)
    values['SOC_LV'] = random.randint(0, 100)
    values['Vmincell'] = random.randint(0, 200)
    values['Vmaxcell'] = random.randint(0, 200)
    values['Tmincell'] = random.randint(0, 200)
    values['Tmaxcell'] = random.randint(0, 200)
    values['Tbat'] = random.randint(0, 200)
    values['Tbat_LV'] = random.randint(0, 200)
    values['Tengine'] = random.randint(0, 200)
    values['Tdriver'] = random.randint(0, 200)
    values['Speed'] = random.randint(0, 200)
    return JsonResponse(values)