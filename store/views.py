from django.shortcuts import render

# create views here
def store(request):
	context = {}
	return render(request, 'store/store.html', context)