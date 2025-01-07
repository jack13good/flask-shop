function addToCart(productId) {
    const quantity = document.getElementById('quantity')?.value || 1;
    
    fetch('/add_to_cart', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `product_id=${productId}&quantity=${quantity}`
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
    })
    .catch(error => {
        console.error('Error:', error);
        alert('加入購物車時發生錯誤');
    });
}

function updateQuantity(productId, change) {
    const input = document.querySelector(`.cart-item[data-product-id="${productId}"] input`);
    let newValue = parseInt(input.value) + change;
    if (newValue < 1) newValue = 1;
    input.value = newValue;
    updateCartItem(productId, newValue);
}

function updateCartItem(productId, quantity) {
    fetch('/update_cart', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `product_id=${productId}&quantity=${quantity}`
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            location.reload();
        }
    });
}

function removeFromCart(productId) {
    if (confirm('確定要移除此商品嗎？')) {
        fetch('/remove_from_cart', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: `product_id=${productId}`
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                location.reload();
            }
        });
    }
}