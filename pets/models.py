from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from django.db import models
import datetime

SPECIES_CHOICES = (
    ('cat', 'cat'),
    ('dog', 'dog'),
    ('hamster', 'hamster')
)

def current_year():
    """return current year"""
    return datetime.date.today().year

def max_value_current_year(value):
    """returns max possible value"""
    return MaxValueValidator(current_year())(value)

class Pet(models.Model):
    name = models.CharField(max_length=200)
    species = models.CharField(
                    max_length = 50,
                    choices = SPECIES_CHOICES,
                    default = 'cat'
                )
    year_of_birth = models.PositiveIntegerField(default=current_year(), 
                        validators=[MinValueValidator(1950), 
                                    max_value_current_year])

    def __str__(self):
        """Return a string representation of a Pet"""
        return f'{self.name}({self.species}, {self.year_of_birth})'

    def get_absolute_url(self): # new
        return reverse('Pet', args=[str(self.id)])
