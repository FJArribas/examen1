from __future__ import unicode_literals
import django
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class usuario(User):
    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.username

class tweet(models.Model):
    texto = models.CharField(max_length=128)
    usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
    fecha = models.CharField(max_length=128)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.texto

class retweet(models.Model):
    tweet = models.ForeignKey(tweet, on_delete=models.CASCADE)
    usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
    fechaDeRetweet = models.CharField(max_length=128)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.tweet.__str__()
