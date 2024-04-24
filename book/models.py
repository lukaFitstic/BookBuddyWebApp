from django.db import models
from django.urls import reverse


# Create your models here.
class Autore(models.Model):
    nome = models.CharField(max_length=100)
    cognome = models.CharField(max_length=100)
    eta = models.IntegerField()
    def __str__(self):
        return self.nome


class Book(models.Model):
    GENERE_CHOICES = (
        ('Giallo', 'Giallo'),
        ('Cucina', 'Cucina'),
        ('Religioso', 'Religioso'),
        ('Azione', 'Azione'),
        ('Commedia', 'Commedia'))
    genere = models.CharField(max_length=100, choices=GENERE_CHOICES)
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Autore,
                               on_delete=models.CASCADE,
                               default=None,
                               null=True)
    year = models.IntegerField(default="2024")
    pages = models.IntegerField(default="0")
    body = models.TextField(default="No body available")
    slug = models.SlugField(default="")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('dettagli', kwargs={"slug": self.slug})


