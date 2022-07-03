from rest_framework import viewsets
from files.models import Files
from files.serializers import FilesSerializer

class FilesViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = Files.objects.all()
    serializer_class = FilesSerializer