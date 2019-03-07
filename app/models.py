from django.db import models

# Create your models here.


class Posting(models.Model):
    company_name = models.TextField()
    position_description = models.TextField()
    location = models.TextField()
    logo = models.URLField()
