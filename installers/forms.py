from django import forms

from .models import Installer

class InstallerForm(forms.ModelForm):
    name    = forms.CharField(widget=forms.TextInput
                                (attrs={"placeholder": "Your name"})) #placeholder is the prompt text in the textbox 
    email   = forms.EmailField(widget=forms.TextInput
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
    class Meta:
        model = Installer
        fields = [
            'name', 
            'email', 
            'mobile', 
            'address', 
            'bio',
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