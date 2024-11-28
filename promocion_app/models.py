from django.db import models

# Create your models here.

class Promocion(models.Model):
    id_promocion=models.PositiveSmallIntegerField(primary_key=True)
    descripcion=models.CharField(max_length=100)
    fecha_inicio=models.CharField(max_length=100)
    fecha_fin=models.CharField(max_length=100)
    descuento=models.PositiveSmallIntegerField()
    productos_aplicados=models.CharField(max_length=100)
    condiciones=models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion
