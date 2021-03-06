import factory
from faker import Factory as FakerFactory
from django.contrib.auth import get_user_model
from files.models import Folder, File
from django.contrib.auth.hashers import make_password

faker = FakerFactory.create()


class UserFactory(factory.django.DjangoModelFactory):
    """User factory."""
    username = factory.Sequence(lambda n: "User%03d" % n)
    first_name = factory.LazyAttribute(lambda x: faker.first_name())
    last_name = factory.LazyAttribute(lambda x: faker.last_name())
    email = factory.LazyAttribute(lambda x: faker.free_email())
    password = factory.LazyFunction(lambda: make_password('test_password'))
    is_staff = True
    is_active = True
    is_superuser = True

    class Meta:
        model = get_user_model()


class FolderFactory(factory.django.DjangoModelFactory):
    """Folder factory."""
    parent = factory.LazyAttribute(lambda x: FolderFactory(parent=None))
    name = factory.LazyAttribute(lambda x: faker.name())
    owner = factory.SubFactory(UserFactory)

    class Meta:
        model = Folder


class FileFactory(factory.django.DjangoModelFactory):
    """File factory."""
    name = factory.LazyAttribute(lambda x: faker.file_name())
    owner = factory.SubFactory(UserFactory)
    file = factory.django.FileField(filename='test.dat', data='testdata')
    folder = factory.SubFactory(FolderFactory)

    class Meta:
        model = File
