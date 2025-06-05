from flask import session, Blueprint,render_template,redirect,url_for,request
from sqlalchemy import select
from app.itemCart import ItemCart


cart_bp = Blueprint('cart',__name__,template_folder='templates/shopping_bag')



@cart_bp.route("/cart/items",methods=['POST','GET'])
def cart():
    if request.method=='GET':
     return render_template("shopping_bag.html")
    else:
      return redirect(request.url)


@cart_bp.route("/cart/add_item",methods=['POST'])
def addItemCart():
   id=request.form.get('id_item')
   quantity_request=int(request.form.get("quantity"))
   # the variable name is used to redirect the user to the product page of the item selected ->redirect(url_for("products.get_product_by_name",name=name))
   name=request.form.get('name_item')
   session.modified=True
   if 'shopping_cart' in session:
   #  if the item is in session, then the item quantity will change
    if id in session['shopping_cart']:
       session['shopping_cart'][id]['quantity']+=quantity_request
       session['shopping_cart'][id]['total_price']= session['shopping_cart'][id]['price']* session['shopping_cart'][id]['quantity']
       item=session['shopping_cart']
       session['shopping_cart']=array_merge(session['shopping_cart'],item)
       session['total_cart']=getTotalValue()
    else:
       name=request.form.get('name_item')
       img_url=request.form.get("urlImg_item")
       price=float(request.form.get("price_item"))
       total_price=price
      #  the item ItemCart is initialized 
       product=ItemCart(id,name,quantity_request,price,total_price,img_url)
      #  the item is a dictionary that has the product id as an key
       item={ product.id:product.to_dict() }
      #  array_merge -> is return a dictionary with the two elements merged
       session['shopping_cart'] = array_merge(session['shopping_cart'],item)
        # getTotalValue()  -> returns the value of the items of the session
       session['total_cart']=getTotalValue()
   else:
   #  the session[shopping_cart] is created 
    name=request.form.get('name_item')
    img_url=request.form.get("urlImg_item")
    price=float(request.form.get("price_item"))
    total_price=price
    quantity_request=int(request.form.get("quantity"))
    product=ItemCart(id,name,quantity_request,price,total_price,img_url)
    item={ product.id:product.to_dict() }
    session['total_cart'] = item[id]['total_price']
    session['shopping_cart'] = item

   return redirect(url_for("products.get_product_by_name",name=name))


@cart_bp.route("/cart/empty")
def empty_cart():
   try:
      session.clear()
      return redirect(url_for('.cart'))
   except Exception as e:
      print(e)
   
#  root to increase the quantity of an existing item in the cart session
@cart_bp.route("/cart/add_qt",methods=['POST'])
def add_qt():
   try:
      #   gets the id of the item 
        id=request.form.get('add_qt_btn')
        if id in session['shopping_cart']:
         session.modified=True
         session['shopping_cart'][id]['quantity']= session['shopping_cart'][id]['quantity']+1
         session['shopping_cart'][id]['total_price']= session['shopping_cart'][id]['quantity']*session['shopping_cart'][id]['price']
         session['total_cart'] = getTotalValue() 
        return redirect(url_for('.cart'))
   except Exception as e:
      print(e)

#  root to decrease the quantity of an existing item in the cart session
@cart_bp.route("/cart/decrease_qt",methods=['POST'])
def decrease_qt():
   try:
        id=request.form.get('decrease_qt_btn')
        if id in session['shopping_cart']:
         session.modified=True
         # if the quantity of the item that will be decease is bigger than 1,
         #  then the quantity will decease with 1 and and the total will be calculate
         if session['shopping_cart'][id]['quantity'] > 1:
          session['shopping_cart'][id]['quantity'] = session['shopping_cart'][id]['quantity']-1
          session['shopping_cart'][id]['total_price'] = session['shopping_cart'][id]['quantity']*session['shopping_cart'][id]['price']
          session['total_cart'] = getTotalValue()
         else:
         #  if the quantity is equal to 1, the item is deleted from the session
          session['shopping_cart'].pop(id,None)
          session['total_cart'] = getTotalValue()
         #  if is the last item in the session, then the session is clear
          if len(session['shopping_cart'].items()) == 0:
            session.clear()
        return redirect(url_for('.cart'))
   except Exception as e:
      print(e)
      
@cart_bp.route("/cart/delete_item_cart/<string:id>")
def delete_item_cart(id):
   try:
      if id in session['shopping_cart']:
         session.modified=True
         # the item is deleted from the session
         session['shopping_cart'].pop(id,None)
         if len(session['shopping_cart'].items()) >0:
            session['total_cart']=getTotalValue()
         else:
              #  if is the last item in the session, then the session is clear
            session.clear()
      return redirect(url_for('.cart'))
   except Exception as e:
      print(e)
     



def array_merge( first_array , second_array ):
 if isinstance( first_array , dict ) and isinstance( second_array , dict ):
  return dict( list( first_array.items() ) + list( second_array.items() ) )
 return False  

def getTotalValue():
   total=0
   for key,value in session['shopping_cart'].items():
     total = total + session['shopping_cart'][key]['price']*session['shopping_cart'][key]['quantity']
   return total
