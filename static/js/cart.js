const updateBtns = document.getElementsByClassName('update-cart')

// event listener for add to cart button
for (i = 0; i < updateBtns.length; i++) {
	updateBtns[i].addEventListener('click', function () {
		var productId = this.dataset.product
		var action = this.dataset.action
		console.log('productId:', productId, 'Action:', action)
// User is logged in or not
		console.log('USER:', user)
		if (user == 'AnonymousUser') {
			console.log('User is not authenticated')

		} else {
			console.log('User is authenticated, sending data...')
		}

	})
}