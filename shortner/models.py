from django.db import models
from django.contrib.auth.models import User


class URL(models.Model):
    full_url = models.URLField(max_length=200)
    short_url = models.SlugField(max_length=6)
    clicks = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.full_url)[:40]
