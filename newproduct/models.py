from django.db import models

class Newproduct(models.Model):
	name = models.CharField(max_length= 255)
