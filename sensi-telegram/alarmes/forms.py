from django import forms
from .models import alarme

class alarmeForm(forms.ModelForm):

    class Meta:
        model = alarme
        fields = '__all__'
