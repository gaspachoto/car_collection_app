from django.core import exceptions, validators
from django.db import models

# •	Profile
# o	Password
# 	Character (password) field, required.


def validate_car_year(value):
    if value < 1980 or value > 2049:
        raise exceptions.ValidationError('Year must be between 1980 and 2049')


def validate_min_username_length(value):
    if len(value) < 2:
        raise exceptions.ValidationError('The username must be a minimum of 2 chars')


class Profile(models.Model):
    MAX_LEN_USERNAME = 10
    MIN_LEN_USERNAME = 2
    MIN_AGE_VALUE = 18
    MAX_PASS_LENGTH = 30
    MAX_NAME_LENGTH = 30

    username = models.CharField(
        max_length=MAX_LEN_USERNAME,
        validators=(
            validate_min_username_length,
        ),
        null=False,
        blank=False,
    )
    email = models.EmailField(
        null=False,
        blank=False,
    )
    age = models.IntegerField(
        validators=(
            validators.MinValueValidator(18),
        ),
        null=False,
        blank=False,
    )
    password = models.CharField(
        max_length=MAX_PASS_LENGTH,
        null=False,
        blank=False,
    )
    first_name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        null=True,
        blank=True,
        verbose_name='First Name',
    )
    last_name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        null=True,
        blank=True,
        verbose_name='Last Name',
    )
    profile_picture = models.URLField(
        null=True,
        blank=True,
        verbose_name='Profile Picture'
    )


class Car(models.Model):
    MAX_TYPE_LENGTH = 10
    MAX_MODEL_LENGTH = 20
    MIN_MODEL_LENGTH = 2

    SPORTS_CAR = 'Sports Car'
    PICKUP = 'Pickup'
    CROSSOVER = 'Crossover'
    MINIBUS = 'Minibus'
    OTHER = 'Other'

    TYPES = (
        (SPORTS_CAR, SPORTS_CAR),
        (PICKUP, PICKUP),
        (CROSSOVER, CROSSOVER),
        (MINIBUS, MINIBUS),
        (OTHER, OTHER),
    )

    type = models.CharField(
        max_length=MAX_TYPE_LENGTH,
        choices=TYPES,
        null=False,
        blank=False,
    )
    model = models.CharField(
        max_length=MAX_MODEL_LENGTH,
        validators=(
            validators.MinLengthValidator(MIN_MODEL_LENGTH),
        ),
        null=False,
        blank=False,
    )
    year = models.IntegerField(
        validators=(
            validate_car_year,
        ),
        null=False,
        blank=False,
    )
    image_url = models.URLField(
        verbose_name='Image URL',
        null=False,
        blank=False,
    )
    price = models.FloatField(
        validators=(
            validators.MinValueValidator(1.0),
        ),
        null=False,
        blank=False,
    )
