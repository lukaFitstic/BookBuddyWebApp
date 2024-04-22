import os
import sys
from django.core.management.base import BaseCommand
from faker import Faker
import faker.providers
import faker.providers.lorem


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
    help = "Command information"

    def handle(self, *args, **kwargs):
        fake = Faker('it_IT')
        fake.add_provider(Provider)

        print("Ciao")
