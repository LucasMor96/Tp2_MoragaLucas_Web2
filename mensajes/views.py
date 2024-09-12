from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Mensaje
from django.views.generic import TemplateView, ListView, DetailView, DeleteView, CreateView
from django.urls import reverse_lazy

class InicioView(TemplateView):
    template_name = 'inicio.html'

class ListarMensajesView(ListView):
    model = Mensaje
    template_name = 'mensajes/listar_mensajes.html'
    context_object_name = 'mensajes'

    def get_queryset(self):
        filtro = self.request.GET.get('filtro', 'todos')  # Valor filtro predeterminado 'todos'
        busqueda = self.request.GET.get('barrabuscar', '')
        queryset = Mensaje.objects.all()

        if filtro == 'enviados':
            queryset = queryset.filter(eliminado=False)
            if busqueda:
                queryset = queryset.filter(remitente__icontains=busqueda)
        elif filtro == 'recibidos':
            queryset = queryset.filter(eliminado=False)
            if busqueda:
                queryset = queryset.filter(destinatario__icontains=busqueda)
        elif filtro == 'favoritos':
            queryset = queryset.filter(favorito=True)  # Mostrar solo los mensajes favs
        else:
            queryset = queryset.filter(eliminado=False)  # Excluir mensajes eliminados por defecto

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

# borra definitivamente el mensaje
class EliminarMensajeView(DeleteView):
    model = Mensaje
    success_url = reverse_lazy('listar_mensajes')

## Envia a la papelera el mensaje
def eliminarPapelera(request, pk):
    mensaje = get_object_or_404(Mensaje, pk=pk)
    mensaje.eliminado = True
    mensaje.save()
    return redirect(reverse_lazy('listar_mensajes'))

def recuperarMensaje(request, pk):
    mensaje = get_object_or_404(Mensaje, pk=pk)
    mensaje.eliminado = False
    mensaje.save()
    return redirect(reverse_lazy('listar_mensajes'))


def marcarFavorito(request, pk):
    mensaje = get_object_or_404(Mensaje, pk=pk)
    mensaje.favorito = True
    mensaje.save()
    return redirect(reverse_lazy('listar_mensajes'))


## Nueva vista para la papelera de mensajes
class PapeleraMensajesView(ListView):
    model = Mensaje
    template_name = 'mensajes/papelera.html'
    context_object_name = 'mensajes'

    def get_queryset(self):
        return Mensaje.objects.filter(eliminado=True)