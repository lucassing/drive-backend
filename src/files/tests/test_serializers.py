from files.serializers import FilesSerializer, FoldersSerializer
from factories import FileFactory, FolderFactory
import pytest

pytestmark = pytest.mark.django_db

class TestFilesSerializer:

    def test_serialize_model(self):
        file = FileFactory.build()
        serializer = FilesSerializer(file)
        assert serializer.data
        
    def test_serialized_data(self):
        file_instance = FileFactory()
        valid_serialized_data = {
                                    'name': file_instance.name, 
                                    'owner': file_instance.owner,
                                    'file': file_instance.file,
                                    'folder': file_instance.folder.id,
                                }
        serializer = FilesSerializer(data=valid_serialized_data)
        assert serializer.is_valid()
        assert serializer.errors == {}

class TestFoldersSerializer:

    def test_serialize_model(self):
        folder_instance = FolderFactory.build()
        serializer = FoldersSerializer(folder_instance)
        assert serializer.data

    def test_serialized_data(self):
        folder_instance = FolderFactory(parent__parent=None)
        valid_serialized_data = {
                                    'parent': folder_instance.parent.id, 
                                    'name': folder_instance.name,
                                    'owner': folder_instance.owner.id,
                                }

        serializer = FoldersSerializer(data=valid_serialized_data)
        assert serializer.is_valid()
        assert serializer.errors == {}