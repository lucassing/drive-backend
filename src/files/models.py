import os
import logging
from django.db.models.signals import post_delete
from django.db import models
from django.dispatch import receiver

logger = logging.getLogger(__name__)


class File(models.Model):
    name = models.CharField(max_length=255, blank=False, default=None)
    modified = models.DateTimeField(auto_now=True)
    uploaded = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='files', null=False, blank=False)
    owner = models.ForeignKey('auth.User', related_name='files', on_delete=models.CASCADE)
    folder = models.ForeignKey('Folder', related_name='files', on_delete=models.CASCADE, null=True, blank=True)


class Folder(models.Model):
    parent = models.ForeignKey('Folder', related_name='folders', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255, blank=False, default=None)
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='folders', on_delete=models.CASCADE)


@receiver(post_delete, sender=File)
def file_instance_removed_handler(sender, instance, using, *args, **kwargs):
    if os.path.exists(instance.file.path):
        os.remove(instance.file.path)
        logger.info("The file was removed")
    else:
        logger.warning(f"File {instance.file.path} does not exist")
