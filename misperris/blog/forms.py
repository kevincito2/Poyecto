from django import forms
from .models import Usuario, Mascotas, Ciudad
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class UsuarioForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ('rut', 'nombre_completo', 'fecha_nacimiento', 'telefono', 'email', 'region', 'ciudad', 'tipo_vivienda')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['ciudad'].queryset = Ciudad.objects.none()

        if 'region' in self.data:
                try:
                    region_id = int(self.data.get('region'))
                    self.fields['ciudad'].queryset = Ciudad.objects.filter(region_id=region_id).order_by('nombre')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty Ciudad queryset
        elif self.instance.pk:
            self.fields['ciudad'].queryset = self.instance.region.ciudad_set.order_by('nombre')
            
class MascotasForm(forms.ModelForm):

    class Meta:
        model = Mascotas
        fields = ('foto','nombre','raza','descripcion','estado')


