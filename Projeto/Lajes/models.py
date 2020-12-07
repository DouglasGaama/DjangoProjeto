from django.db import models
from PIL import Image

# Create your models here.
class Laje(models.Model):
    nome_laje = models.CharField(max_length=200)
    foto = models.ImageField(null=True, blank=True)
    desc_L = models.TextField
    Tipo = models.CharField(max_length=200)
    conceito = models.CharField(max_length=200)

    def __str__(self):
        return self.nome_laje