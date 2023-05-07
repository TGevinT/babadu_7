
from django.db import models


class Atlet(models.Model):
    nama = models.CharField(max_length=255)

    def __str__(self):
        return self.nama



# Create your models here.
