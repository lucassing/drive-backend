from files import views

from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'files', views.FilesViewSet, basename="files")
router.register(r'folders', views.FoldersViewSet, basename="folders")

urlpatterns = [
    path('', include(router.urls)),
]