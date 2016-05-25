# models.py

from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.postgres.fields import JSONField



class Brewpub(models.Model):
    name = models.CharField(max_length=30)
    address = models.TextField()
    telephone = models.CharField(min=10, max=10)
    website = models.UrlField()
    hours = JSONField() # form: Mon: {11:00 - 23:00}
    rating = models.ManyToManyField(Rating)
    beers = models.ManyToManyField(Beer)


class Beer(models.Model):
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    description = models.TextField()
    # abv = not sure if want to include this in this version.
    rating = models.ManyToManyField(Rating)


class Rating(models.Model):
    user_id = models.ForeignKey(User)
    rating = models.IntegerField()
    timestamp = models.DateTime()
    review = models.TextField()


class User(models.AbstractBaseUser):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30)
    email = models.EmailField(max_length=100, unique=True)
    date_created = models.DateTimeField()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELD = ['username', 'password', 'email']

