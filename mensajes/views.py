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
        queryset = Mensaje.objects.all()
        filtro = self.request.GET.get('filtro', 'todos')  # Valor filtro predeterminado 'todos'
        # Filtrar según pestaña activa
        if filtro == 'eliminados':
            queryset = queryset.filter(eliminado=True)
        elif filtro == 'favoritos':
            queryset = queryset.filter(favorito=True)
        else:  # 'todos'
            queryset = queryset.filter(eliminado=False)

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

## Restaurar de la papelera
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
    

def buscar_mensajes(request):
    filtro = request.GET.get('filtro', 'recibidos')  # Obtenemos el filtro activo, por defecto 'todos'
    busqueda = request.GET.get('barrabuscar', '')  # Obtenemos el término de búsqueda, por defecto vacío
    encontrado = False
    mensajes = []
    encontrado = False
    if busqueda:
        print("Buscando mensajes que contengan:", busqueda)
        print("Filtro activo:", filtro)
        print("Valores recibidos en el request GET:", request.GET)  # Agrega esto para ver todos los valores
        if filtro == 'recibidos':
            mensajes = Mensaje.objects.filter(destinatario__icontains=busqueda, eliminado=False)
            encontrado = True
            print("Filtro activo:", filtro)
            print("Mensajes encontrados:", mensajes)
                
        elif filtro == 'enviados':
            mensajes = Mensaje.objects.filter(remitente__icontains=busqueda, eliminado=False)
            encontrado = True
        else:
            encontrado = False
    else:
        print("No se ha especificado un término de búsqueda.")
        mensajes = []

    return render(request, 'mensajes/listar_mensajes.html', 
        {'mensajes': mensajes, 
        'filtro_activo': filtro, 
        'encontrado': encontrado,
        'busqueda': busqueda
        })
