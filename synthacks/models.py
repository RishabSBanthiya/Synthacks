from django.db import models
from django.contrib.auth.models import User


class Team(models.Model):
    first_name = models.CharField(max_length=64, unique=True, null=True)
    second_name = models.CharField(max_length=64, unique=True,null=True)
    third_name = models.CharField(max_length=64, unique=True, null=True)
    first_grade=models.IntegerField(null=True)
    second_grade = models.IntegerField(null=True)
    third_grade = models.IntegerField(null=True)

