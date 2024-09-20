from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# customer model
class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=100, null=True)
	email = models.CharField(max_length=100)

	def __str__(self):
		return self.name

# product model
class Product(models.Model):
	name = models.CharField(max_length=100)
	price = models.FloatField()
	# digital = models.BooleanField(default=False,null=True, blank=True)

	def __str__(self):
		return self.name

# order model
class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=100, null=True)

	def __str__(self):
		return str(self.id)


