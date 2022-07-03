from django.contrib import admin

# Register your models here.
from .models import Files

@admin.register(Files)
class FilesAdmin(admin.ModelAdmin):
    pass

