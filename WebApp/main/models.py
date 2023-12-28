from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=200)
    capital = models.CharField(max_length=100)
    region = models.CharField(max_length=200)
    population = models.IntegerField()

    def __str__(self):
        return self.name

