from flask import Flask
from app.config import Conf
from app.database import init_db
from app.products import products
from app.checkout import checkout
from app.account import user
from app.order import orders
from app.cart import cart
from flask_login import LoginManager
from app.models.users import User
import os
import stripe
login_manager=LoginManager()
app=Flask(__name__)
stripe.api_key= 'sk_test_51RTLo1Fj7cBJIZqzVvZbRrTKww5JaZc0qKtLqNxwuG8yVEvdkrh1ZQKMefcyqaPIN9svR7T7HE1W1hF3mvLGufIg00Giy0vkw1'
app.config.from_object(Conf)

init_db()
app.register_blueprint(products.products_bp)
app.register_blueprint(checkout.checkout_bp)
app.register_blueprint(user.user_bp)
app.register_blueprint(cart.cart_bp)
app.register_blueprint(orders.order_bp)
login_manager.init_app(app)
login_manager.login_view = 'account.login'

@login_manager.user_loader
def load_user(id):
    return  User.query.get(int(id))  
 
from app import routes

if __name__ == '__main__':

  try:
    app.run(host="0.0.0.0")
  finally:
    print('Application shutting down...', flush=True)