# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
# Create your models here.


class lectura (models.Model):
    Tems = models.DateTimeField(default=datetime.now())
    RPM = models.IntegerField(max_length=40000)
    SOC = models.IntegerField(max_length=500)
    Tbat = models.IntegerField(max_length=500)
    Tdriver = models.IntegerField(max_length=500)
    Tengine = models.IntegerField(max_length=500)
    Vbat = models.IntegerField(max_length=1000)
    Imax = models.IntegerField(max_length=5000)
    Vmincell = models.IntegerField(max_length=10000)
    Vmaxcell = models.IntegerField(max_length=10000)
    Tmincell = models.IntegerField(max_length=10000)
    Tmaxcell = models.IntegerField(max_length=10000)