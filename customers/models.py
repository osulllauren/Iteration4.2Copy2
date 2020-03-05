from django.db import models

# Create your models here.

class Customer(models.Model):
    name            = models.CharField(max_length=50)
    serviceableArea = models.CharField(max_length=50)
    cork            = models.BooleanField(default=False)
    kerry           = models.BooleanField(default=False)
    dublin          = models.BooleanField(default=False)
    limerick        = models.BooleanField(default=False)
    meath           = models.BooleanField(default=False)
    waterford       = models.BooleanField(default=False)
    jobType         = models.CharField(max_length=50)
    boiler_installations                     = models.BooleanField(default=False)                    
    heating_control_installations            = models.BooleanField(default=False)            
    boiler_and_heating_control_installations = models.BooleanField(default=False)