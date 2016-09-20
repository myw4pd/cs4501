from django.db import models


# Create your models here.


class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=100)


	def publish(self):
		self.save()

   	def __str__(self):
        	return self.title
