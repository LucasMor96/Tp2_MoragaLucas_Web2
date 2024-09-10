from django.shortcuts import render
from django.http import HttpResponse
from .models import Mensaje
from django.views.generic import TemplateView,ListView, DetailView, DeleteView, CreateView
from django.urls import reverse_lazy

class InicioView(TemplateView):
    template_name = 'inicio.html'

class ListarMensajesView(ListView):
    model = Mensaje
    template_name = 'mensajes/mensajes_recibidos.html'
    context_object_name = 'mensajes'

    def get_queryset(self):
        queryset = super().get_queryset()
        filtro = self.request.GET.get('filtro')

        if filtro == 'recibidos':
            queryset = queryset.filter(destinatario__icontains='nombre_destinatario')  # Ajusta según sea necesario
        elif filtro == 'enviados':
            queryset = queryset.filter(remitente__icontains='nombre_remitente')  # Ajusta según sea necesario
        else:
            queryset = queryset.none()

        return queryset

class DetalleMensajeView(DetailView):
    model = Mensaje
    template_name = 'mensajes/detalle_mensaje.html'
    context_object_name = 'mensaje'

class EnviarMensajeView(CreateView):
    model = Mensaje
    template_name = 'mensajes/enviar_mensaje.html'
    fields = ['asunto', 'texto', 'remitente', 'destinatario']  
    success_url = '/mensajes/'  

class EliminarMensajeView(DeleteView):
    model = Mensaje
    success_url = reverse_lazy('listar_mensajes')