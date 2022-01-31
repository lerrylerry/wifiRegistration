from django import forms
from Wifi_App.models import Faculty

class FacultyForm(forms.ModelForm):

    class Meta:
        model = Faculty

        fields = "__all__"