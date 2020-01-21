from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator,URLValidator, validate_comma_separated_integer_list

# Create your models here.

class Game(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.CharField(max_length=30)
    comments = models.PositiveIntegerField()
    rate = models. CharField(max_length=10, validators=[validate_comma_separated_integer_list])
    plataform = models.CharField(max_length=10)
    
    def __str__(self):
        return self.title
