from django.db import models

# Create your models here.
from django.core import validators

class Topic(models.Model):
    S_no=models.IntegerField()
    Topic_Name=models.CharField(max_length=25, primary_key=True, validators=[validators.MaxLengthValidator(6)])

    def __str__(self) -> str:
        return self.Topic_Name
