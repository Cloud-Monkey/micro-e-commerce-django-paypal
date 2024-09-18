from django.shortcuts import render

# create views here
def store(request):
	context = {}
	return render(request, 'store/store.html', context)

def cart(request):
    context = {}
    return render(request, 'cart/store.html', context)

def checkout(request):
    context = {}
    return render(request, 'checkout/store.html', context)