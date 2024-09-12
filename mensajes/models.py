from django.db import models

class Mensaje(models.Model):
    asunto = models.CharField(max_length=100, blank =True)
    texto = models.TextField()
    remitente = models.CharField(max_length=100)
    destinatario = models.CharField(max_length=100)
    fecha_envio = models.DateTimeField(auto_now_add=True)
    eliminado = models.BooleanField(default=False)
    favorito = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.asunto} - {self.remitente} a {self.destinatario}"