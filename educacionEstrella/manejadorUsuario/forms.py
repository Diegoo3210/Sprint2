from django import forms
from .models import usuarioRegistrado
 
class usuarioRegistrado(forms.ModelForm):
    class Meta:
        model=usuarioRegistrado
        fields = ['name', 'last_name', 'address', 'email', 'phone', 'university', 'scan_id']