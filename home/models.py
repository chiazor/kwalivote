from django.db import models

class home(models.Model):
	username = models.CharField(max_length=30)
	password = models.CharField(max_length=50)


