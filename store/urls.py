from django.urls import path

from . import views

urlpatterns = [
    #Leave as empty string for base url
	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
	path('product/<int:product_id>/', views.product_detail, name="product_detail"),
 	path('product/<int:product_id>/delete_review/<int:review_id>', views.review_delete, name='review_delete'),
	path('product/<int:product_id>/edit_review/<int:review_id>', views.review_edit, name='review_edit'),
]