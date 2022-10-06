from django.db import models

# Create your models here.
class Either(models.Model):
    title = models.CharField(max_length=30)
    issue_a = models.CharField(max_length=30)
    issue_b = models.CharField(max_length=30)