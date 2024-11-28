from django.db import models

# Create your models here.

class Reseña (models.Model):
    id_reseña=models.PositiveSmallIntegerField(primary_key=True)
    id_producto=models.CharField(max_length=100)
    id_cliente=models.CharField(max_length=100)
    calificacion=models.CharField(max_length=100)
    comentario=models.CharField(max_length=100)
    fecha_reseña=models.CharField(max_length=100)
    estado=models.CharField(max_length=100)

    def __str__(self):
        return self.comentario
