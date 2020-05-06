from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone as tz
from datetime import date
from django.core.validators import MaxValueValidator

# Create your models here.
FOOD_TYPES = (
    (1, "pizza"),
    (2, "pasta"),

)

table_choices = (
    (1, "two guests table no 1"),
    (2, 'two guests table no 2'),
    (3, "two guests table no 3"),
    (4, 'two guests table no 4'),
    (5, "two guests table no 5"),
    (6, 'two guests table no 6'),
    (7, "four guests table no 7"),
    (8, 'four guests table no 8'),
    (9, "four guests table no 9"),
    (10, 'four guests table no 10'),
    (11, 'four guests table no 11'),
    (12, 'eight guests table no 12'),
    (13, 'three guests table no 13'),
)

class Meals(models.Model):
    name = models.CharField(max_length=64)
    ingredients = models.TextField()
    price = models.IntegerField()
    type_of_food = models.IntegerField(choices=FOOD_TYPES)
    image = models.ImageField(upload_to= "images", default="")


class Reservation(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone =  models.CharField(max_length=12)
    table_number = models.IntegerField(choices=table_choices, default=1)
    time = models.TimeField()
    date_reserved = models.DateField()
    date_booked = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(blank=True)

    def __str__(self):
        return self.first_name
