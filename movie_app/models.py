from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Movie(models.Model):
    E = 'E'
    D = 'D'
    R = 'R'
    CURRENCY_CHOICES = [
        (E, 'euro'),
        (D, 'dollar'),
        (R, 'ruble')
    ]
    name = models.CharField(max_length=100)
    rating = models.IntegerField(null=True, blank=True)
    year = models.IntegerField(null=False)
    budget = models.IntegerField(default=10000)
    slug = models.SlugField(default='', null=False, db_index=True)
    test = models.IntegerField(null=True)
    currency = models.CharField(max_length=1, choices=CURRENCY_CHOICES, default=R)

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse('show_one_movie', args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Movie, self).save(*args, **kwargs)



