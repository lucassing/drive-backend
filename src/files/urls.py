import imp
from files import views

from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'', views.FilesViewSet,basename="files")

urlpatterns = [
    path('', include(router.urls)),
]