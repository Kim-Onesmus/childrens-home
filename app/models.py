from django.db import models
from django.contrib.auth.models import User
# Create your models here.

delivery_choices = [
    ('i will delicer','i will deliver'),
    ('come for donation','come for donation'),
]

class Client(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    username = models.CharField(max_length=30)
    # mobile_no = models.CharField(max_length=10)
    email = models.CharField(max_length=100)

    def __str__(self):
        return(self.username)


class Question(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    number = models.CharField(max_length=15)
    question = models.TextField(max_length=100)

    def __str__(self):
        return(self.question)

class Book(models.Model):
    full_name = models.CharField(max_length=50)
    mobile_no = models.PositiveIntegerField()
    number = models.PositiveIntegerField(default=0)
    location = models.CharField(max_length=50)

    def __str__(self):
        return(self.full_name)

class Donation(models.Model):
    full_name = models.CharField(max_length=50)
    mobile_no = models.PositiveIntegerField()
    donations = models.CharField(max_length=20)
    delivery = models.CharField(max_length=20, choices=delivery_choices)

    def __str__(self):
        return(self.full_name)