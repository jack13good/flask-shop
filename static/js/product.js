function decreaseQuantity() {
    const input = document.getElementById('quantity');
    const currentValue = parseInt(input.value);
    if (currentValue > 1) {
        input.value = currentValue - 1;
    }
}

function increaseQuantity() {
    const input = document.getElementById('quantity');
    const currentValue = parseInt(input.value);
    const maxValue = parseInt(input.getAttribute('max'));
    if (currentValue < maxValue) {
        input.value = currentValue + 1;
    }
}

function addToCart(productId) {
    const quantity = document.getElementById('quantity')?.value || 1;
    // 這裡之後會實作加入購物車的功能
    alert(`已將 ${quantity} 件商品加入購物車`);
}