from random import choices
from django.db import models

# Create your models here.
class Either(models.Model):
    title = models.CharField(max_length=200)
    issue_a = models.CharField(max_length=200)
    issue_b = models.CharField(max_length=200)

class Comment(models.Model):
    Pick_Red = 'RED'
    Pick_Blue = 'BLUE'
    Pick_Choices = ((Pick_Red, 'RED'), (Pick_Blue, 'BLUE'))
    pick = models.CharField(
        choices=Pick_Choices,
        max_length=4
    )
    content = models.CharField(max_length=200)
    either = models.ForeignKey(Either, on_delete=models.CASCADE)