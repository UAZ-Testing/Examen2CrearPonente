from django.db import models


# Create your models here.

class Ponente(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    primer_apellido = models.CharField(max_length=50, null=False)
    segundo_apellido = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        print('%s %s %s' % (
        self.nombre, self.primer_apellido, self.segundo_apellido))
