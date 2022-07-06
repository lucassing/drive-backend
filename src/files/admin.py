from django.contrib import admin

# Register your models here.
from .models import File, Folder


@admin.register(File)
class FilesAdmin(admin.ModelAdmin):
    readonly_fields = ('modified', 'uploaded')


@admin.register(Folder)
class FoldersAdmin(admin.ModelAdmin):
    readonly_fields = ('modified', 'created')
