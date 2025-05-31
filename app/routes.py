from app import app
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, session
from app.models.products import Product

def get_products_suggestion(list):
    session.modified=True
    for id in list:
      product = Product.get_product_by_id(id)
      item={ list.index(id): product.to_dict()}
      if 'suggestion'  in session:
        session['suggestion'] = array_merge(session['suggestion'],item)
      else:
         print
         session['suggestion'] = item

@app.route("/")
def index():
   list_ids=[1,3,5,9,4,22,10,20,21,19]
   if 'suggestion' not in session:
     get_products_suggestion(list_ids)
   return render_template("index.html")     


@app.route("/about_us")
def about_us():
    return render_template("about_us.html")  

def array_merge( first_array , second_array ):
 if isinstance( first_array , dict ) and isinstance( second_array , dict ):
  return dict( list( first_array.items() ) + list( second_array.items() ) )
  

