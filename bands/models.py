from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Band(models.Model):
    name = models.CharField(max_length=300)
    country = models.CharField(max_length=150,blank=True)
    city = models.CharField(max_length=150,blank=True)
    members = ArrayField(models.CharField(max_length=1000,blank=True),null=True)
    image = models.CharField(blank=True)
    biography = models.CharField(blank=True, max_length=5000)

    def __str__(self):
        return str(self.name)

class Album(models.Model):
    title = models.CharField(blank=True)
    artist = models.ForeignKey(
        'Band',
        related_name='releases',
        on_delete=CASCADE,
        null=True,
        blank=True
    )
    year = models.CharField(max_length=4)
    color = models.CharField(blank=True)
    variants = models.ManyToManyField(
        'self',
        blank=True
    )
    tracklist = ArrayField(models.CharField(blank=True))
    country = models.CharField(blank=True)
    genre = models.CharField(blank=True)
    image = models.CharField(blank=True)
    on_sale = models.BooleanField(blank=True,null=True)

    def __str__(self):
        return str(self.title)
