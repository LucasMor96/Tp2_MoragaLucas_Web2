"""
URL configuration for TableroMensajes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mensajes.views import (
    InicioView, ListarMensajesView, DetalleMensajeView, 
    EnviarMensajeView, EliminarMensajeView, eliminarPapelera, PapeleraMensajesView, marcarFavorito, recuperarMensaje,buscar_mensajes
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', InicioView.as_view(), name='inicio'),
    path('mensajes/', ListarMensajesView.as_view(), name='listar_mensajes'),
    path('mensajes/<int:pk>/', DetalleMensajeView.as_view(), name='detalle_mensaje'),
    path('mensajes/enviar/', EnviarMensajeView.as_view(), name='enviar_mensaje'),
    path('mensajes/eliminar/<int:pk>/', EliminarMensajeView.as_view(), name='eliminar_mensaje'),
    path('mensajes/papelera/', PapeleraMensajesView.as_view(), name='ver_papelera'),
    path('mensajes/enviar_papelera/<int:pk>/', eliminarPapelera, name='enviar_papelera'),
    path('mensajes/recuperar_mensaje/<int:pk>/', recuperarMensaje, name='recuperar_mensaje'),
    path('mensajes/marcar_favorito/<int:pk>/', marcarFavorito, name='marcar_favorito'),
    path('mensajes/buscar/', buscar_mensajes, name='buscar_mensajes'),
]
