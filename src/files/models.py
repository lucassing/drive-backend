from distutils.command.upload import upload
from operator import mod
from django.db import models

# Create your models here.
class Files(models.Model):
    name = models.CharField(max_length=255)
    upload_time = models.TimeField(auto_now=True)
    file = models.FileField(upload_to='files')