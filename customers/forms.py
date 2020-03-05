from django import forms

from .models import Customer


class CustomerForm(forms.ModelForm):
    name            = forms.CharField(widget=forms.TextInput
                                (attrs={"placeholder": "Your name"})) 
    serviceableArea = forms.CharField(required=False)
    cork        = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    kerry       = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    dublin      = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    limerick    = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    meath       = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    waterford   = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    jobType         = forms.CharField(required=False)
    boiler_installations                     = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    heating_control_installations            = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    boiler_and_heating_control_installations = forms.BooleanField(widget=forms.CheckboxInput, required=False) 
                            

    class Meta:
        model = Customer
        fields = [
            'name', 
            'serviceableArea',
            'cork',
            'kerry',
            'dublin',
            'limerick',
            'meath', 
            'waterford',
            'jobType', 
            'boiler_installations',
            'heating_control_installations',
            'boiler_and_heating_control_installations',
        ]