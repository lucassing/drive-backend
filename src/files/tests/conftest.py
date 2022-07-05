import pytest

from pytest_factoryboy import register
from factories import UserFactory, FolderFactory, FileFactory
from rest_framework.test import APIClient


#Fixtures
@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def api_client(client):
    user = UserFactory()
    # Authenticate
    client.login(username=user.username, password='test_password')
    return client

@pytest.fixture
def user_instance():
    return UserFactory()

@pytest.fixture
def file_instance():
    return FileFactory()

@pytest.fixture
def folder_instance():
    return FolderFactory()

@pytest.fixture
def folder_with_files():
    folder = FolderFactory()
    FileFactory.create_batch(3,folder=folder)
    return folder

# Register Factories
register(UserFactory)
register(FolderFactory)
register(FileFactory)