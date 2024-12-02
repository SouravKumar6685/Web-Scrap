from django.db import models
from django.utils import timezone

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=10000)
    description = models.TextField()
    images = models.URLField(null=True, blank=True)
    external_link = models.URLField(null=True, blank=True)


