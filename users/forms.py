from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    #skillset = forms.SkillsetField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email'] #will allow us to update our username & email


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image'] #will allow us to update our image


# WORKING_RADIUS= [
#     ('cork', 'Cork'),
#     ('kerry', 'Kerry'),
#     ('limerick', 'Limerick'),
#     ('dublin', 'Dublin'),
#     ]

# class UserInstallerForm(forms.Form):
#     #workingRadius = forms.TextField(required=False)
#     working_radius= forms.CharField(label='What is your serviceable area?', widget=forms.Select(choices=WORKING_RADIUS))
#     #workingDays = forms.TextField(required=False)
#     #workingSkillset = forms.TextField(required=False)

#     class Meta:
#         model = User
#         # fields = ['workingRadius', 'workingDays', 'workingSkillet']
#         fields = ['workingRadius']







        