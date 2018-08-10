from django import forms
from .models import usuario

class usuarioForm(forms.ModelForm):
    nome = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    telefone = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    chat_id = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    class Meta:
        model = usuario
        fields = '__all__'
