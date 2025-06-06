from flask import Blueprint,render_template,session
from sqlalchemy import select
from app.database import db_session
from app.models.products import Product, Category_Product

# in the navigation, the user can select products by  category: handle, clutch or sholder
products_bp=Blueprint('products',__name__,template_folder='templates/products')
@products_bp.route('/products/<string:type>')
def get_products_by_type(type):
    category = Category_Product.get_category(type)
    # access the products of a specific category
    bags = category.products
    category.category_name=category.category_name.upper()
    return render_template("products.html", bags = bags, category = category)

@products_bp.route('/product/<string:name>')
def get_product_by_name(name):
    select_pr = select(Product).where(Product.name == name)
    # each product has an unique name scalars(select_pr).first() -> get the first item with the selected name
    product = db_session.scalars(select_pr).first()
    return render_template("product.html",product = product)

