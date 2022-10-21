from django.views.generic import *
from .models import *
from django.http import HttpResponseNotFound

class HomePageView(TemplateView):
    template_name = 'home.html'

    
class TareasPageView(ListView):
    template_name = 'tareas.html'
    model = Tarea
    context_object_name = 'Todas_Las_Tareas'

class TareasPageDetail(DetailView):
    template_name = 'tareas_detalle.html'
    model = Tarea
    context_object_name = 'Tarea_Detallada'