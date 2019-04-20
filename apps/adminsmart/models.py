from django.db import models

class Eventos(models.Model):

    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length = 300, default=None)
    fecha = models.DateTimeField()
    descripcion = models.TextField()
    ponentes =   models.CharField(max_length = 300)
    concepto_pago = models.CharField(max_length = 300)

    class  Meta:
        verbose_name_plural = "Eventos2"
    def __str__(self):
        return self.titulo
