from django.db import models


class User(models.Model):
     username = models.CharField(max_length=25, unique=True)
     password = models.CharField(max_length=100)
     user_id = models.AutoField(primary_key=True)
     first_name = models.CharField(max_length=20)
     last_name = models.CharField(max_length=20)
     location = models.CharField(max_length=20)
    # car = models.ForeignKey('Car')
     date_joined = models.DateTimeField()    


# Create your models here.
