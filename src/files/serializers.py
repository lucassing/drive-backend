from rest_framework import serializers
from files.models import File, Folder

class FilesSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = File
        fields = ('id', 'name', 'uploaded', 'modified', 'owner', 'file', 'folder')
        read_only_fields = ('file',)

class FoldersSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Folder
        fields = ['id', 'parent', 'name', 'created', 'modified', 'owner']
    