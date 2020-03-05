from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django .urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    #available_days = models.TextField()
    monday = models.BooleanField(default=False)
    tuesday = models.BooleanField(default=False)
    wednesday = models.BooleanField(default=False)
    thursday = models.BooleanField(default=False)
    friday = models.BooleanField(default=False)
    saturday = models.BooleanField(default=False)
    sunday = models.BooleanField(default=False)
    #serviceable_area = models.TextField()
    cork        = models.BooleanField(default=False)
    kerry       = models.BooleanField(default=False)
    dublin      = models.BooleanField(default=False)
    limerick    = models.BooleanField(default=False)
    meath       = models.BooleanField(default=False)
    waterford   = models.BooleanField(default=False)
    #skillset = models.TextField()
    boiler_installations                     = models.BooleanField(default=False)                    
    heating_control_installations            = models.BooleanField(default=False)            
    boiler_and_heating_control_installations = models.BooleanField(default=False)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk}) 
    #we want the page to go back to the post detail page
    #reverse will return the full path as a string
