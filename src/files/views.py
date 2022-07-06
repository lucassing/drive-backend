from rest_framework import viewsets, permissions
from files.models import File, Folder
from files.serializers import FilesSerializer, FoldersSerializer


class FilesViewSet(viewsets.ModelViewSet):
    """
    This viewset that provides default `create()`, `retrieve()`, `update()`, `partial_update()`, `destroy()` and `list()` actions for files.
    """
    queryset = File.objects.all()
    serializer_class = FilesSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        return super().perform_create(serializer)


class FoldersViewSet(viewsets.ModelViewSet):
    """
    This viewset that provides default `create()`, `retrieve()`, `update()`, `partial_update()`, `destroy()` and `list()` actions for folders.
    """
    queryset = Folder.objects.all()
    serializer_class = FoldersSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        return super().perform_create(serializer)
