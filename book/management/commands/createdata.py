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

IDAUTORI = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
    21, 22, 23
]


class Provider(faker.providers.BaseProvider):
    def book_genere(self):
        return self.random_element(GENERI)

    def book_idautor(self):
        return self.random_element(IDAUTORI)


class Command(BaseCommand):
    help = 'Custom command to run manage.py shell, import a specific model, and create some objects'

    def handle(self, *args, **options):
        fake = Faker(["it_IT"])
        fake.add_provider(Provider)

        for _ in range(100):
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
