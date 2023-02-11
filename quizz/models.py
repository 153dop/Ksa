from django.db import models


class Question(models.Model):
    id = models.IntegerField(default=0, primary_key=True)
    description = models.CharField(max_length=200)
    result = models.FloatField(default=0.0)
    response = models.CharField(max_length=200)
