from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Band(models.Model):
    name = models.CharField(max_length=300,blank=True)
    country = models.CharField(max_length=150,blank=True)
    city = models.CharField(max_length=150,blank=True)
    members = models.CharField(blank=True)
    image = models.CharField(blank=True)
    # releases = models.ForeignKey(
    #     'Album',
    #     related_name='artist',
    #     on_delete=CASCADE,
    #     null=True,
    #     blank=True
    # )

    def __str__(self):
        return self.name

class Album(models.Model):
    title = models.CharField(blank=True)
    artist = models.ForeignKey(
        'Band',
        related_name='releases',
        on_delete=CASCADE,
        null=True,
        blank=True
    )
    year = models.CharField(blank=True)
    color = models.CharField(blank=True)
    variants = models.ManyToManyField(
        'self',
        # on_delete=models.CASCADE,
        # null=True,
        blank=True
    )
    tracklist = models.CharField(blank=True)
    country = models.CharField(blank=True)
    genre = models.CharField(blank=True)
    image = models.CharField(blank=True)
    on_sale = models.BooleanField(blank=True,null=True)

    def __str__(self):
        return self.title
