from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

class Tarea(models.Model):
    Nombre = models.CharField(max_length=50)
    Descripcion = models.TextField(max_length=300)
    Encargado = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    FechaElaboracion = models.DateTimeField(auto_now_add=True)
    Hecho = models.BooleanField()

    def __str__(self):
        return self.Nombre

    def get_absolute_url(self):
        return reverse('tareas')

class Tecnologico(models.Model):
    Clave_Tecnologico = models.CharField(max_length=3)
    Nombre = models.CharField(max_length=50)
    Ciudad = models.CharField(max_length=30)

    def __str__(self):
        return self.Nombre

    def get_absolute_url(self):
        return reverse('tareas')

class Comentarios(models.Model):
    tarea = models.ForeignKey(
        Tarea,
        on_delete = models.CASCADE,
        related_name='comentarios',
    )
    comentario = models.CharField(max_length=500)
    creador = models.ForeignKey(
        get_user_model(),
        on_delete = models.CASCADE,
    )

    def __str__(self):
        return self.comentario

    def get_absolute_url(self):
        return reverse('tareas')
