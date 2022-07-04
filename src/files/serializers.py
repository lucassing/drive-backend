from rest_framework import serializers, permissions
from files.models import File, Folder

class FilesSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = File
        permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        fields = ['id', 'name', 'uploaded', 'modified', 'owner', 'file', 'folder']
        
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        return super().perform_create(serializer)

class FoldersSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Folder
        permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        fields = ['id', 'parent', 'name', 'created', 'modified', 'owner']
