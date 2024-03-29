from django.db import models


class UrlModel(models.Model):
    original_url = models.URLField()
    short_url = models.CharField(max_length=10, unique=True)  # 10 not 6 because there might be a num added to it

    def __str__(self):
        return '%s: %s' % (self.original_url, self.short_url)
