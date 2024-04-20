from django.db import models
import uuid

MAX_CHAR_LENGTH = 200
GROUP_CHOICES = [
    ("Food", "음식"),
]


class Food(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4)
    food_id = models.CharField(max_length=MAX_CHAR_LENGTH, unique=True)
    food_cd = models.CharField(max_length=MAX_CHAR_LENGTH, null=True)
    group_name = models.CharField(max_length=MAX_CHAR_LENGTH, choices=GROUP_CHOICES, default="Food")
    food_name = models.CharField(max_length=MAX_CHAR_LENGTH, null=True)
    research_year = models.IntegerField(null=True)
    market_name = models.CharField(max_length=MAX_CHAR_LENGTH, null=True)
    ref_name = models.CharField(max_length=MAX_CHAR_LENGTH, null=True)
    serving_size = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    calorie = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    carbohydrate = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    protein = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    province = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    sugars = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    salt = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    cholesterol = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    saturated_fatty_acids = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    trans_fat = models.DecimalField(max_digits=7, decimal_places=2, null=True)
