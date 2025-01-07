from flask import Flask, render_template, session, redirect, url_for, jsonify, request
from models import db, Product

print("開始初始化 Flask 應用程式...", flush=True)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'

db.init_app(app)

# 首頁路由
@app.route('/')
def home():
    return render_template('index.html')

# 商品列表路由
@app.route('/products')
def products():
    products = Product.query.filter_by(is_active=True).all()
    return render_template('products.html', products=products)

# 商品詳情路由
@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('product_detail.html', product=product)

# 購物車相關路由
@app.route('/cart')
def cart():
    cart_data = session.get('cart', {})
    cart_items = []
    total = 0
    
    for product_id, quantity in cart_data.items():
        product = Product.query.get(int(product_id))
        if product:
            item_total = product.price * quantity
            cart_items.append({
                'product': product,
                'quantity': quantity,
                'total': item_total
            })
            total += item_total

    return render_template('cart.html', cart_items=cart_items, total=total)

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    product_id = request.form.get('product_id')
    quantity = int(request.form.get('quantity', 1))
    
    cart = session.get('cart', {})
    
    if product_id in cart:
        cart[product_id] = cart[product_id] + quantity
    else:
        cart[product_id] = quantity
    
    session['cart'] = cart
    
    return jsonify({'status': 'success', 'message': '商品已加入購物車'})

@app.route('/update_cart', methods=['POST'])
def update_cart():
    product_id = request.form.get('product_id')
    quantity = int(request.form.get('quantity', 0))
    
    cart = session.get('cart', {})
    
    if quantity > 0:
        cart[product_id] = quantity
    else:
        cart.pop(product_id, None)
    
    session['cart'] = cart
    
    return jsonify({'status': 'success'})

@app.route('/remove_from_cart', methods=['POST'])
def remove_from_cart():
    product_id = request.form.get('product_id')
    cart = session.get('cart', {})
    cart.pop(product_id, None)
    session['cart'] = cart
    
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    print("正在啟動伺服器...", flush=True)
    print("請在瀏覽器中訪問 http://localhost:5000", flush=True)
    app.run(debug=True, port=5000, use_reloader=True)