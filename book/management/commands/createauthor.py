from django.core.management.base import BaseCommand
from faker import Faker
from book.models import Autore


class Command(BaseCommand):
    help = 'Custom command to generate random author'

    def add_arguments(self, parser):
        parser.add_argument('quantity', type=int, help='Inserisci il numero di autori da generare')

    def handle(self, *args, **kwargs):
        fake = Faker(["it_IT"])
        quantity = kwargs['quantity']

        for _ in range(quantity):
            Autore.objects.create(
                nome=fake.first_name(),
                cognome=fake.last_name(),
                eta=fake.random_int(min=18, max=99)
            )
