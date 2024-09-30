from django.shortcuts import render, get_object_or_404, reverse
from django.http import JsonResponse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django import forms
from django.contrib import messages
from django.views import generic
import json
import datetime
from .models import * 


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('rating', 'body')
        
        
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

	reviews = Review.objects.filter(product=product_id).order_by("-created_at")
	review_count = reviews.count()
	has_existing_review = False

	for review in reviews:
		if review.user == request.user:
			has_existing_review = True

	if request.method == "POST" and has_existing_review is not True:
		review_form = ReviewForm(data=request.POST)
	
		if review_form.is_valid():
			review = review_form.save(commit=False)
			review.user = request.user
			review.product = expanded_product
			review.save()
			messages.add_message(
        		request, messages.SUCCESS,
        		"Review submitted."
    		)
			return HttpResponseRedirect(reverse('product_detail', args=[product_id]))
    
	review_form = ReviewForm()

	return render(
        request,
        "store/product_detail.html",
        {
            "product": expanded_product,
            'cartItems':cartItems,
            "reviews": reviews,
            "review_count": review_count,
            "review_form": review_form,
            "has_existing_review": has_existing_review,
        },
        
    )

def review_delete(request, product_id, review_id):

    queryset = Product.objects.filter(id=product_id)
    expanded_product = get_object_or_404(queryset, id=product_id)
    review = get_object_or_404(Review, pk=review_id)

    if review.user == request.user:
        review.delete()
        messages.add_message(request, messages.SUCCESS, 'Review deleted.')
    else:
        messages.add_message(request, messages.ERROR, 'Failed to delete review.')

    return HttpResponseRedirect(reverse('product_detail', args=[product_id]))
 
def review_edit(request, product_id, review_id):
    if request.method == "POST":

        queryset = Product.objects.filter(id=product_id)
        expanded_product = get_object_or_404(queryset, id=product_id)
        review = get_object_or_404(Review, pk=review_id)
        review_form = ReviewForm(data=request.POST, instance=review)

        if review_form.is_valid() and review.user == request.user:
            review = review_form.save(commit=False)
            review.user = request.user
            review.product = expanded_product
            review.save()
            messages.add_message(
        		request, messages.SUCCESS,
        		"Review edited successfully."
    		)
        else:
            messages.add_message(request, messages.ERROR, 'Error updating review!')
            
    return HttpResponseRedirect(reverse('product_detail', args=[product_id]))