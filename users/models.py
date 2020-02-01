from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django import forms
from multiselectfield import MultiSelectField

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

#RESIZING IMAGES
#TO save space on file system & also speed up the website
#https://www.youtube.com/watch?v=CQ90L5jfldw&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=9
    def save(self):
        super().save() #parent class

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size) #this will resize the image 
            img.save(self.image.path) 


#copied from the profile class above
class Job(models.Model):
    job_installer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='installer')
    job_customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer')
    job_desc = models.CharField(max_length=200)
    job_date = models.DateTimeField('date of job')
    job_booked = models.BooleanField()

    def __str__(self): 
        return self.job_desc


#http://www.learningaboutelectronics.com/Articles/How-to-create-a-drop-down-list-in-a-Django-form.php
#DROPDOWN SELECTIONS
SKILLSET_CHOICES = [
    ('gas boiler installations','Gas Boiler Installations' ), 
    ('oil boiler installations', 'Oil Boiler Installations'), 
    ('all boiler installations', 'All Boiler Installations'),
    ('heating control installations', 'Heating Control Installations'), 
    ('gas boiler & heating control installations', 'Gas Boiler & Heating Control Installations'), 
    ('oil boiler & heating control installations', 'Oil Boiler & Heating Control Installations'), 
    ('all boiler & heating control installations', 'All Boiler & Heating Control Installations'),
]

RADIUS_CHOICES = [
    ('cork', 'Cork'), 
    ('kerry', 'Kerry'), 
    ('limerick', 'Limerick'), 
    ('dublin', 'Dublin'),

]


class InstallerDetail(models.Model):
    installer_identity = models.ForeignKey(User, on_delete=models.CASCADE, related_name='installer_alias')
    installer_date1 = models.DateField('available date1')
    installer_date2 = models.DateField('available date2')
    installer_date3 = models.DateField('available date3')
    installer_availability = models.CharField(max_length=200)
    installer_skillset = models.CharField(max_length=50, choices=SKILLSET_CHOICES)
    #https://docs.djangoproject.com/en/2.2/topics/forms/modelforms/
    installer_radius = models.CharField(max_length=50, choices=RADIUS_CHOICES)
    
    
    def __str__(self):
        return self.installer_availability

#NEW CODE JANUARY- TRYING TO WRITE A MULTI-SELECT FOR AVAILABLE DAYS
#https://www.youtube.com/watch?v=5jWJBpS0tkg
class AvailableDay(models.Model):
    AVAILABLEDAY_CHOICES = (
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    )
    title = MultiSelectField(choices = AVAILABLEDAY_CHOICES)
