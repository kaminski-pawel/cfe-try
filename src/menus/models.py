from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse

from restaurants.models import RestaurantLocation

class Item(models.Model):
    user            = models.ForeignKey(settings.AUTH_USER_MODEL)
    restaurant      = models.ForeignKey(RestaurantLocation)
    name            = models.CharField(max_length=120)
    contents        = models.TextField(help_text='Separate each item by comma')
    excludes        = models.TextField(blank=True, null=True, help_text='Separate each item by comma')
    public          = models.BooleanField(default=True)
    timestamp       = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated', '-timestamp'] # '-' at beggining means 'reversed'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Url to redirect to after creating new Item
        Can be used in template as {{ object.get_absolute_url }}"""
        return reverse('menus:detail', kwargs={'pk': self.pk}) # kwargs are passing the slug

    def get_contents(self):
        """When getting `contents` instance, the processing will be run"""
        return self.contents.split(',')

    def get_excludes(self):
        """When getting `contents` instance, the processing will be run"""
        return self.excludes.split(',')
