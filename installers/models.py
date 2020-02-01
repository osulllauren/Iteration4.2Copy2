from django.db import models

# Create your models here.
class Installer(models.Model):
    name    = models.CharField(max_length=50) #max_length = required 
    email   = models.EmailField()
    mobile  = models.TextField()
    address = models.TextField()
    bio     = models.TextField(blank=True, null=True)  
 