from django.db import models
from django.core.validators import URLValidator, validate_comma_separated_integer_list

# Create your models here.

class Game(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.CharField(max_length=30)
    comments = models.PositiveIntegerField()
    rate = models. CharField(max_length=10, validators=[validate_comma_separated_integer_list])
    plataform = models.CharField(max_length=10)
    link = models.CharField(max_length=500, validators=[URLValidator])
    picture = models.CharField(max_length=500, validators=[URLValidator])
    gamePrice = models.FloatField()
    
    def __str__(self):
        return self.title
