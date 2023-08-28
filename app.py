from flask import Flask, render_template

app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/buy_now')
def buy_now():
    return render_template('buy_now.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/payment')
def payment():
    return render_template('payment.html')

@app.route('/add_to_cart')
def add_to_cart():
    return render_template('add_to_cart.html')

@app.route('/milk_comparison')
def milk_comparison():
    return render_template('milk_comparison.html')

@app.route('/yourorder')
def your_order():
    cart_items = []  
    return render_template("yourorder.html", cart_items=cart_items)

if __name__ == '__main__':
    app.run(debug=True)



