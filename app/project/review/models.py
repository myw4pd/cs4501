from django.db import models

from django.utils import timezone

# Create your models here.
# class CarReview(models.Model):
#     title = models.CharField(max_length=255)
#     car_id = models.CharField(max_length=20)
#     user_id = models.ForeignKey('User')
#     rating = models.CharField(max_length=20)
#     text = models.TextField()
#     date = models.DateTimeField(default=timezone.now)
#
#     def __str__(self):
#         return self.title

class UserReview(models.Model):
    title = models.CharField(max_length=255)
    user_id = models.ForeignKey('User')
    text = models.CharField(max_length=200)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
         return self.title