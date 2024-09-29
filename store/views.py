from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.http import HttpResponse
import json
import datetime
from .models import * 

def store(request):

	if request.user.is_authenticated:

		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else:
		#Create empty cart for now for non-logged in user
		items = []
		order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
		cartItems = order['get_cart_items']

	products = Product.objects.all()
	context = {'products':products, 'cartItems':cartItems}
	return render(request, 'store/store.html', context)

def cart(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else:
		#Create empty cart for now for non-logged in user
		try:
			cart_cookie = request.COOKIES.get('cart', '{}')
			cart = json.loads(cart_cookie)
		except:
			cart = {}

		items = []
		order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
		cartItems = order['get_cart_items']

		for i in cart:
			#We use try block to prevent items in cart that may have been removed from causing error
			try:
				cartItems += cart[i]['quantity']

				product = Product.objects.get(id=i)
				total = (product.price * cart[i]['quantity'])

				order['get_cart_total'] += total
				order['get_cart_items'] += cart[i]['quantity']

				item = {
					'id':product.id,
					'product':{'id':product.id,'name':product.name, 'price':product.price, 
					'imageURL':product.imageURL}, 'quantity':cart[i]['quantity'],
					'digital':product.digital,'get_total':total,
					}
				items.append(item)

				if product.digital == False:
					order['shipping'] = True
			except:
				pass


	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'store/cart.html', context)

def checkout(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else:
		#Create empty cart for now for non-logged in user
		items = []
		order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
		cartItems = order['get_cart_items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'store/checkout.html', context)

def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']

	customer = request.user.customer
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)

def processOrder(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		total = float(data['form']['total'])
		order.transaction_id = transaction_id

		if total == order.get_cart_total:
			order.complete = True
		order.save()

		if order.shipping == True:
			ShippingAddress.objects.create(
			customer=customer,
			order=order,
			address=data['shipping']['address'],
			city=data['shipping']['city'],
			county=data['shipping']['county'],
			post_code=data['shipping']['post_code'],
			)
	else:
		print('User is not logged in')

	return JsonResponse('Payment submitted..', safe=False)

def product_detail(request, product_id):

	if request.user.is_authenticated:

		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		cartItems = order.get_cart_items
	else:
		#Create empty cart for now for non-logged in user
		order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
		cartItems = order['get_cart_items']

	queryset = Product.objects.filter(id=product_id)
	expanded_product = get_object_or_404(queryset, id=product_id)
   
	return render(
        request,
        "store/product_detail.html",
        {"product": expanded_product, 'cartItems':cartItems},
    )
