from django.db import models

# Create your models here.
class Autore(models.Model):
    nome = models.CharField(max_length=100)
    cognome = models.CharField(max_length=100)
    eta = models.IntegerField()
    def __str__(self):
        return self.nome

class Book(models.Model):
    genere = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Autore,
                               on_delete=models.CASCADE,
                               default=None,
                               null=True)
    year = models.IntegerField()
    pages = models.IntegerField()
    body = models.TextField()
    def __str__(self):
        return self.title
