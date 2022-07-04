from pytest_factoryboy import register
from factories import UserFactory, FolderFactory, FileFactory

register(UserFactory)
register(FolderFactory)
register(FileFactory)