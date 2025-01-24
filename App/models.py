from django.db import models

# create models here
class User(models.Model):
    userID = models.PositiveBigIntegerField(primary_key=True)
    email = models.EmailField()
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)

