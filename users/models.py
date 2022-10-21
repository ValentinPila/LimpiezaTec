from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

class Puesto(models.Model):
    Nombre = models.CharField(max_length=30)
        
    def __str__(self):
        return self.Nombre

class CostumUser(AbstractUser):
    Nombre = models.CharField(max_length=30)
    Clave_Usuario = models.CharField(max_length=6) #C-1234
    Clave_Tecnologico = models.CharField(max_length=3)#254
    Puesto = models.ForeignKey(Puesto, on_delete=models.CASCADE, null=True)
    #null=True, blank=True
    
