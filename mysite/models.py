# -*- encoding: utf-8 -*- 
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User

class Maker(models.Model):
	name = models.CharField(max_length=10)
	country = models.CharField(max_length=10)
	
	def __str__ (self):
		return self.name
		
class Profile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	yearclass = models.CharField(max_length=20, default='一年級')
	male = models.BooleanField(default=False)
	website = models.URLField(null=True)
	
	def __str__(self):
		return self.user.name
		
	
	
@python_2_unicode_compatible
class Category1(models.Model):
	name = models.CharField(max_length=200, );
	
	def __str__(self):
		return self.name
		
		
@python_2_unicode_compatible
class Product(models.Model):
	category1 = models.ForeignKey(Category1, on_delete=models.CASCADE, default=0,)
	sku = models.CharField(max_length=20, default='書本編號',)
	name = models.CharField(max_length=200, default='書本名稱')
	description = models.TextField()
	image = models.URLField(null=True)
	website = models.URLField(null=True)
	stock = models.PositiveIntegerField(default=0)
	price = models.DecimalField(max_digits=10, decimal_places=2, default=0,)
	
	def __str__(self):
		return self.name
	


class Category (models.Model):

	def __str__(self):
		return self.name
	

# Create your models here.

