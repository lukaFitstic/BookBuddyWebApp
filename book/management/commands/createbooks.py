from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command
from faker import Faker
import faker.providers
import faker.providers.lorem
from book.models import Book, Autore


GENERI = [
    "Azione",
    "Commedia",
    "Cucina",
    "Giallo",
    "Religioso"
]

IDAUTORI = []

for autore in Autore.objects.all():
    IDAUTORI.append(autore.id)


class Provider(faker.providers.BaseProvider):
    def book_genere(self):
        return self.random_element(GENERI)

    def book_idautor(self):
        return self.random_element(IDAUTORI)


class Command(BaseCommand):
    help = 'Custom command to run manage.py shell, import a specific model, and create some objects'

    def add_arguments(self, parser):
        parser.add_argument('quantity', type=int, help='Inserisci il numero di libri da generare')

    def handle(self, *args, **kwargs):
        fake = Faker(["it_IT"])
        fake.add_provider(Provider)
        quantity = kwargs['quantity']

        for _ in range(quantity):
            faketitle = fake.sentence(nb_words=3, variable_nb_words=False)
            fakeautorid = fake.book_idautor()
            Book.objects.create(title=faketitle.replace(".", ""),
                                author=Autore.objects.get(id=fakeautorid),
                                pages=fake.random_int(min=1, max=999),
                                body=fake.sentence(nb_words=50, variable_nb_words=True),
                                genere=fake.book_genere(),
                                year=fake.random_int(min=1800, max=2024),
                                slug=faketitle.replace(" ", "-").replace(".", "").lower()
                                )
