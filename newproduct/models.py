from django.db import models
from django.contrib.auth.models import User

class Newproduct(models.Model):
	title = models.CharField(max_length= 255)

class Product(models.Model):
	name = models.CharField(max_length= 255)

class Produc(models.Model):
	product = models.CharField(max_length=255)
	pubdate = models.DateTimeField()

class Products(models.Model):
	title = models.CharField(max_length=255)
	pub_date = models.DateTimeField()
	body = models.TextField()
	url = models.TextField()
	image = models.ImageField(upload_to='images/')
	icon = models.ImageField(upload_to= 'images/')
	votes_total = models.IntegerField(default= 1)
	hunter = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	def summary(self):
		return self.body[:100]

	def pub_date_form(self):
		return self.pub_date.strftime('%b %e %Y')		