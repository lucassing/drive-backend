from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class File(models.Model):
    name = models.CharField(max_length=255, blank=False, default=None)
    modified = models.DateTimeField(auto_now=True)
    uploaded= models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='files', null=False, blank=False)
    owner = models.ForeignKey('auth.User', related_name='files', on_delete=models.CASCADE)
    folder = models.ForeignKey('Folder', related_name='files', on_delete=models.CASCADE, null=True, blank=True)

class Folder(models.Model):
    parent = models.ForeignKey('Folder', related_name='folders', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255, blank=False, default=None)
    modified = models.DateTimeField(auto_now=True)
    created= models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='folders', on_delete=models.CASCADE)

