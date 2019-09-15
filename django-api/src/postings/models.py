from django.conf import settings
from django.db import models
from django.urls import reverse
from datetime import datetime
from rest_framework.reverse import reverse as api_reverse

# django hosts --> subdomain for reverse

class BlogPost(models.Model):
    # pk aka id --> numbers
    date = models.DateField()
    channel = models.CharField(max_length=300,null = True)
    country = models.CharField(max_length=300,null = True)
    os = models.CharField(max_length=300,null = True)
    impressions = models.BigIntegerField(default=0)
    clicks = models.BigIntegerField(default=0)
    installs = models.FloatField(default=0.0)
    spend = models.FloatField(default = 0.0)
    revenue = models.FloatField(default = 0.0)

    def __str__(self):
        return str(self.country)
