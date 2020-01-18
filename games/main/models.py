from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator,URLValidator

# Create your models here.

class Game(models.Model):
    title = models.CharField(max_length=100, unique=True)
    price = models.FloatField()
    category = models.TextField()
    comments = models.PositiveIntegerField()
    rate = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    
    def __str__(self):
        return self.title