from django.contrib.auth.models import User
from django.db import models

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    cref = models.CharField(max_length=28)


    def __str__(self):
        return self.nome
