from __future__ import unicode_literals
from django.contrib import admin
from aplicacion.models import usuario, tweet, retweet

# Register your models here.

admin.site.register(usuario)
admin.site.register(tweet)
admin.site.register(retweet)
