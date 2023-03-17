from django.db import models

class MyModel(models.Model):
    fullname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    age = models.IntegerField()
    mobilenumber = models.IntegerField()
	
