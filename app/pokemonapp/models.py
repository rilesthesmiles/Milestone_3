from django.db import models

# Create your models here.
from django.db import models


class PokemonCard(models.Model):
    name = models.CharField(max_length=255)
    HP = models.PositiveIntegerField()
    img_url = models.CharField(max_length=255)
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.name
