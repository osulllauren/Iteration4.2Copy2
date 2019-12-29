from django.contrib import admin
from .models import Profile, Job, InstallerDetail
#register the profile model

admin.site.register(Profile)
admin.site.register(Job)
admin.site.register(InstallerDetail)