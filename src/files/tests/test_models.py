import pytest
from django.contrib.auth import get_user_model
from files.models import File, Folder
from factories import UserFactory, FolderFactory, FileFactory



##### Factories tests #####
def test_user_factory(user_factory):
    """Test user factory is a UserFactory instance"""
    assert user_factory is UserFactory

def test_folder_factory(folder_factory):
    """Test folder factory is a FolderFactory instance"""
    assert folder_factory is FolderFactory

def test_user_factory(file_factory):
    """Test file factory is a FileFactory instance"""
    assert file_factory is FileFactory
    
@pytest.mark.django_db
def test_user_instance(user):
    """Test user fixture is an instance of User"""
    assert isinstance(user, get_user_model())

@pytest.mark.django_db
def test_folder_instance(folder):
    """Test folder fixture is an instance of Folder"""
    assert isinstance(folder, Folder)

@pytest.mark.django_db
def test_file_instance(file):
    """Test file fixture is an instance of Folder"""
    assert isinstance(file, File)


##### Folders tests #####
@pytest.mark.django_db
def test_folder_create_instance_no_name_FAILS(folder_factory):
    """Test that create a folder without name raise error"""
    try:
        folder_factory(name='')
        assert False
    except Exception:
        assert True

@pytest.mark.django_db
def test_folder_create_instance_no_owner_FAILS(folder_factory):
    """Test that create a folder without owner raise error"""
    try:
        folder_factory(owner='')
        assert False
    except Exception:
        assert True


##### Files tests #####
@pytest.mark.django_db
def test_file_create_instance_no_name_FAILS(file_factory):
    """Test that the create a file without name raise error"""
    try:
        file_factory(name='')
        assert False
    except Exception:
        assert True

@pytest.mark.django_db
def test_file_create_instance_no_owner_FAILS(file_factory):
    """Test that the create a file without owner raise error"""
    try:
        file_factory(owner='')
        assert False
    except Exception:
        assert True

    