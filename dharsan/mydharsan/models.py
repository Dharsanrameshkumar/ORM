from django.db import models
from django.contrib import admin
class Footballplayer (models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    country=models.CharField(max_length=20)
    experience=models.IntegerField()
    position=models.CharField(max_length=20)

class FootballplayerAdmin(admin.ModelAdmin):
    list_display=('name','age','country','experience','position')
       
    