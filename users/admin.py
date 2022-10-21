from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CostumUserChangeForm, CostumUserCreationForm
from .models import CostumUser, Puesto

class CostumUserAdmin(UserAdmin):
    auth_form = CostumUserCreationForm
    model = CostumUser
    form = CostumUserChangeForm
    list_display = ['is_staff', 'username', 'email', 'Clave_Usuario', 'Clave_Tecnologico', 'Puesto']

admin.site.register(CostumUser, CostumUserAdmin)
admin.site.register(Puesto)
# Register your models here.
