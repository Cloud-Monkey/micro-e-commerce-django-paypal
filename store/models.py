from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# customer model holds a one to one relationship to each user
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
	digital = models.BooleanField(default=False,null=True, blank=True)

	def __str__(self):
		return self.name

# order model connected to the customer with a one to many relationship
class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=100, null=True)

	def __str__(self):
		return str(self.id)

# order item model. Items in the cart connected to the customer with a one to many relationship
class OrderItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

# shipping address model, child to order model
class ShippingAddress(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	address = models.CharField(max_length=100, null=False)
	city = models.CharField(max_length=100, null=False)
	county = models.CharField(max_length=100, null=False)
	post_code = models.CharField(max_length=50, null=False)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.address
