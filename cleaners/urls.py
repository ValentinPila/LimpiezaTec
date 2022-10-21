from django.urls import path 

from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('tareas/', TareasPageView.as_view(), name='tareas'),
    path('tareas/<int:pk>/', TareasPageDetail.as_view(), name='tarea_detallada')
]