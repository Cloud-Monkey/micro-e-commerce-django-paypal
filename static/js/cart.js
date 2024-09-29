const updateBtns = document.getElementsByClassName('update-cart')

// event listener for add to cart button
for (i = 0; i < updateBtns.length; i++) {
	updateBtns[i].addEventListener('click', function () {
		const productId = this.dataset.product
		const action = this.dataset.action

		// User is logged in or not
		if (user == 'AnonymousUser') {
			addCookieItem(productId, action)
		} else {
			updateUserOrder(productId, action)
		}

	})
}

// gets called when user is logged in POST request stringifys productID and action as a JSON object
function updateUserOrder(productId, action) {
	console.log('User is authenticated, sending data...')

	const url = '/update_item/'
	// create token workaround from django documentation
		fetch(url, {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json',
			'X-CSRFToken': csrftoken,
			}, 
		body: JSON.stringify({ 'productId': productId, 'action': action })
		})
		.then((response) => {
		   return response.json();
		})
		.then((data) => {
		    location.reload()
		});
}

// create cookie for cart when user is logged or not
function addCookieItem(productId, action){
    console.log('User is not authenticated');

    if (action == 'add'){
        if (cart[productId] == undefined){
            cart[productId] = {'quantity':1}
        } else {
            cart[productId]['quantity'] += 1
        }
    }

    if (action == 'remove'){
        cart[productId]['quantity'] -= 1

        if (cart[productId]['quantity'] <= 0){
            console.log('Item should be deleted')
            delete cart[productId];
        }
    }

    // Set the cookie with SameSite=Lax attribute
    document.cookie = 'cart=' + JSON.stringify(cart) + 
                      ';path=/;' +
                      'max-age=604800;' + // 1 week
                      'SameSite=Lax;' +
                      (window.location.protocol === 'https:' ? 'Secure;' : '');
    
    location.reload()
}
