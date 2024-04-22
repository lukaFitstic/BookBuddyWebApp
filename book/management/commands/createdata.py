from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command
from faker import Faker
import faker.providers
import faker.providers.lorem
from book.models import Book


GENERI = [
    "Azione",
    "Commedia",
    "Cucina",
    "Giallo",
    "Religioso"
]


class Provider(faker.providers.BaseProvider):
    def book_genere(self):
        return self.random_element(GENERI)


class Command(BaseCommand):
    help = 'Custom command to run manage.py shell, import a specific model, and create some objects'

    def handle(self, *args, **options):
        print("Pippo")
