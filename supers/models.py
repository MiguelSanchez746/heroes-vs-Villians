from django.db import models
from django.forms import CharField
from super_types.models import SuperTypes
# Create your models here.

class Super(models.Model):
    name = models.CharField(max_length=255)
    alter_ego = models.CharField(max_length=255)
    primary_ability = models.CharField(max_length=255)
    secondary_ability = CharField(max_length=22)
    catchphrase = CharField(max_length=255)
    super_type = models.ForeignKey(SuperTypes, on_delete=models.CASCADE)