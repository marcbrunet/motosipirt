# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.timezone import now


# Create your models here.

class lectura(models.Model):
    RPM = models.IntegerField()
    Tems = models.DateTimeField(auto_now_add=True)
    SOC = models.IntegerField()
    Tbat = models.IntegerField()
    Tdriver = models.IntegerField()
    Tengine = models.IntegerField()
    Vbat = models.IntegerField()
    Imax = models.IntegerField()
    Vmincell = models.IntegerField()
    Vmaxcell = models.IntegerField()
    Tmincell = models.IntegerField()
    Tmaxcell = models.IntegerField()

    def crea(self, data):
        self.Tems = now()
        self.RPM = data['RPM']
        self.SOC = data['SOC']
        self.Tbat = data['Tbat']
        self.Tdriver = data['Tdriver']
        self.Tengine = data['Tengine']
        self.Vbat = data['Vbat']
        self.Imax = data['Imax']
        self.Vmincell = data['Vmincell']
        self.Vmaxcell = data['Vmaxcell']
        self.Tmincell = ['Tmincell']
        self.Tmaxcell = data['Tmaxcell']

    def __unicode__(self):
        return str(self.Tems)
