import pytest
import json
from factories import FileFactory, FolderFactory, UserFactory
from rest_framework.reverse import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from dateutil import parser
from files.urls import router
from files import models

pytestmark = pytest.mark.django_db


class TestFilesEndpoints:
    expected_keys = ['id', 'name', 'uploaded', 'modified', 'owner', 'file', 'folder']

    def test_get_list(self, api_client):
        FileFactory.create_batch(3)
        response = api_client.get(reverse('files-list'))
        assert response.status_code == 200
        assert len(response.data) == 3

    def test_create(self, api_client, file_instance):
        expected_json = {
            'name': file_instance.name,
            'file': SimpleUploadedFile('data.dump', b'123', content_type='multipart/form-data'),
        }

        response = api_client.post(
            reverse('files-list'),
            data=expected_json,
        )

        assert response.status_code == 201
        assert response.data != {}

    def test_retrieve(self, api_client, file_instance):
        url = reverse('files-detail', args=[file_instance.id])
        response = api_client.get(url)
        assert response.status_code == 200 or response.status_code == 301
        for key in self.expected_keys:
            assert key in response.data

    def test_update(self, api_client, file_instance, user_instance):
        url = reverse('files-detail', args=[file_instance.id])
        data = {
            'name': 'new_name',
            'owner': user_instance.id,
        }

        response = api_client.put(
            url,
            data=data,
            format='json'
        )

        assert response.status_code == 200 or response.status_code == 301
        assert file_instance.name != response.data['name']
        assert file_instance.owner != response.data['owner']
        assert file_instance.uploaded == parser.isoparse(response.data['uploaded'])

    def test_delete(self, api_client, file_instance):

        url = reverse('files-detail', args=[file_instance.id])

        response = api_client.delete(url)

        assert response.status_code == 204


class TestFoldersEndpoints:

    expected_keys = ['id', 'parent', 'name', 'created', 'modified', 'owner']

    def test_get_list(self, api_client):
        FolderFactory.create_batch(3, parent=None)
        response = api_client.get(reverse('folders-list'))
        assert response.status_code == 200
        assert len(response.data) == 3

    def test_create(self, api_client, folder_instance):
        expected_json = {
            'parent': folder_instance.id,
            'name': 'new_name'
        }

        response = api_client.post(
            reverse('folders-list'),
            data=expected_json,
        )

        assert response.status_code == 201
        assert response.data != {}

    def test_retrieve(self, api_client, folder_instance):
        url = reverse('folders-detail', args=[folder_instance.id])
        response = api_client.get(url)

        assert response.status_code == 200 or response.status_code == 301
        for key in self.expected_keys:
            assert key in response.data

    def test_update(self, api_client, folder_instance, user_instance):
        url = reverse('folders-detail', args=[folder_instance.id])
        new_folder = FolderFactory()
        data = {
            'name': 'new_name',
            'parent': new_folder.id
        }

        response = api_client.put(
            url,
            data=data,
            format='json'
        )

        assert response.status_code == 200 or response.status_code == 301
        assert folder_instance.name != response.data['name']
        assert folder_instance.parent != response.data['parent']
        assert folder_instance.created == parser.isoparse(response.data['created'])

    def test_delete(self, api_client, folder_with_files):
        url = reverse('folders-detail', args=[folder_with_files.id])
        response = api_client.delete(url)
        assert response.status_code == 204
        assert not models.File.objects.all()  # Test that the Files depend on that folder where removed
