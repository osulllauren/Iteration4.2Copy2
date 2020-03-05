from django.db import models

from django import forms

# Create your models here.

class Installer(models.Model):
    #name    = models.CharField(max_length=50) #max_length = required 
    #available_days = models.TextField(null=True)
    monday = models.BooleanField(default=False)
    tuesday = models.BooleanField(default=False)
    wednesday = models.BooleanField(default=False)
    thursday = models.BooleanField(default=False)
    friday = models.BooleanField(default=False)
    saturday = models.BooleanField(default=False)
    sunday = models.BooleanField(default=False)
    serviceable_areas  = models.TextField()
    cork        = models.BooleanField(default=False)
    kerry       = models.BooleanField(default=False)
    dublin      = models.BooleanField(default=False)
    limerick    = models.BooleanField(default=False)
    meath       = models.BooleanField(default=False)
    waterford   = models.BooleanField(default=False)
    skillset = models.TextField(blank=True, null=True)
    boiler_installations                     = models.BooleanField(default=False)                    
    heating_control_installations            = models.BooleanField(default=False)            
    boiler_and_heating_control_installations = models.BooleanField(default=False)