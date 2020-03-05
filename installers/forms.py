from django import forms

from .models import Installer


class InstallerForm(forms.ModelForm):
    
    #name    = forms.CharField(widget=forms.TextInput
                                #(attrs={"placeholder": "Your name"})) #placeholder is the prompt text in the textbox 
    #email   = forms.EmailField(widget=forms.TextInput
    #                            (attrs={"placeholder": "Your email"}))
    #available_days = forms.CharField()
    #RECORDING WORKING AVAILABILITY
    monday      = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    tuesday     = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    wednesday   = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    thursday    = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    friday      = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    saturday    = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    sunday      = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    #RECORDING SERVICEABLE AREAS
    serviceable_areas = forms.CharField()
    cork        = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    kerry       = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    dublin      = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    limerick    = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    meath       = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    waterford   = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    #RECORDING SKILLSETS
    skillset = forms.CharField()
    boiler_installations                     = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    heating_control_installations            = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    boiler_and_heating_control_installations = forms.BooleanField(widget=forms.CheckboxInput, required=False) 
    #mobile  = forms.CharField()
    #address = forms.CharField()
    #bio     = forms.CharField(
    #               required=False, 
    #               widget=forms.Textarea(
    #                   attrs={
    #                       "placeholder": "Your experience & information about you",
    #                       "rows": 5, #size of the text field
    #                       'cols': 30
    #                   }
    #                ))


    #what is going to save to the database
    class Meta:   
        model = Installer
        fields = [
            #'name', 
            'monday',
            'tuesday',
            'wednesday', 
            'thursday', 
            'friday',
            'saturday',
            'sunday', 
            'serviceable_areas', 
            'cork',
            'kerry',
            'dublin',
            'limerick',
            'meath', 
            'waterford',
            'skillset', 
            'boiler_installations',
            'heating_control_installations',
            'boiler_and_heating_control_installations',
        ]



class RawInstallerForm(forms.Form):
    name    = forms.CharField(widget=forms.TextInput
                                (attrs={"placeholder": "Your name"})) #placeholder is the prompt text in the textbox 
    email   = forms.CharField(widget=forms.TextInput
                                (attrs={"placeholder": "Your email"}))
    mobile  = forms.CharField()
    address = forms.CharField()
    bio     = forms.CharField(
                    required=False, 
                    widget=forms.Textarea(
                        attrs={
                            "placeholder": "Your experience & information about you",
                            "rows": 5, #size of the text field
                            'cols': 30
                        }
                    ))