from flask import Blueprint,render_template,session
from sqlalchemy import select
from app.database import db_session
from app.models.products import Product, Category_Product


products_bp=Blueprint('products',__name__,template_folder='templates/products')
@products_bp.route('/products/<string:type>')
def get_products_by_type(type):
    category = Category_Product.get_category(type)
    bags = category.products
    return render_template("products.html",bags=bags)

@products_bp.route('/product/<string:name>')
def get_product_by_name(name):
    select_pr = select(Product).where(Product.name == name)
    product= db_session.scalars(select_pr).first()
    print(product.to_dict())
    return render_template("product.html",product = product)

