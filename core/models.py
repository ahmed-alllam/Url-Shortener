from django.db import models


class UrlModel(models.Model):
    original_url = models.URLField()
    short_url = models.CharField(max_length=6, unique=True)

    def __str__(self):
        return '%s: %s' % (self.original_url, self.short_url)
