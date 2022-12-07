from flask import render_template
from app import app
from models.orders import orders

@app.route('/orders')
def index():
    return render_template('index.html', title = "Yoga Studio:Orders", orders=orders)

@app.route('/orders/<index>')
def get(index):
    x = int(index)
    return render_template('order.html', title = "Order", order=orders[x])