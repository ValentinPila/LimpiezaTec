from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CostumUser

class CostumUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CostumUser
        fields = UserCreationForm.Meta.fields + ('Nombre','email','Clave_Usuario','Clave_Tecnologico', 'Puesto')


class CostumUserChangeForm(UserChangeForm):
    class Meta:
        model = CostumUser
        fields = UserChangeForm.Meta.fields