from django.db import models
from django.conf import settings

from .utils import code_generator, create_shortcode
from .validators import url_validate

SHORTCODE_MAX = getattr(settings, 'SHORTCODE_MAX', 10)


class PnplURLManager(models.Manager):
    def all(self, *args, **kwargs):
        qs = super(PnplURLManager, self).all(*args, **kwargs)
        qs = qs.filter(active=True)
        return qs

class PnplURL(models.Model):
    url = models.CharField(max_length=200, validators=[url_validate])
    shortcode = models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    objects = PnplURLManager()


    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == '':
            self.shortcode = create_shortcode(self)
        if not 'http'in self.url:
            self.url = 'http://' + self.url
        super(PnplURL, self).save(*args, **kwargs)


    def __str__(self):
        return str(self.url)


