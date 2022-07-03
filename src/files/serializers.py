from rest_framework import serializers
from files.models import Files

class FilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Files
        fields = ['id', 'name', 'upload_time', 'file']