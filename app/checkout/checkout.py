from flask import session, Blueprint,render_template,redirect,url_for,request
from sqlalchemy import select
import uuid
from app.models.address import Address_Shipping, Delivery_Type, delivery_types
from app.models.payments import Payment
from app.models.orders import Invoice, Invoice_Details, Item_Order
from app.forms.address_form import AddressForm
from app.forms.payment_form import PaymentForm
from flask_login import login_required, current_user
from datetime import datetime,timezone,timedelta
import stripe
checkout_bp = Blueprint('checkout',__name__,template_folder='templates/checkout')
order = {
   
}

def get_delivery_day(delivery_type):
   if delivery_type=='express':
     date = datetime.now()
     tomorrow = date + timedelta(1)
     return tomorrow



@checkout_bp.route('/checkout/shipping', methods=['POST', 'GET'])
@login_required   
def get_shipping_information():  
      form_address = AddressForm(request.form)
      if request.method == 'POST' and form_address.validate():
        street = form_address.street.data
        city = form_address.city.data
        county = form_address.county.data
        postcode = form_address.postcode.data
        delivery_type_selected = form_address['cost'].data
        delivery = delivery_types[delivery_type_selected]
        cost = delivery.cost
        arrival_date=delivery.estimate_arrival
        address=Address_Shipping(street,city,county,postcode,arrival_date,cost)
        session['total_cart'] = session['total_cart'] + float(cost)
        order['address'] = address
        return render_template('payment.html',delivery = order['address'])
      else:
        return render_template("shipping.html",form_address=form_address, delivery_types = delivery_types)
      

 
      
@checkout_bp.route('/checkout/payment', methods=['POST', 'GET'])
def get_payment_information():  
   if request.method=='GET':
      return  render_template("payment.html",delivery = order['address'])
   
   total=int( session['total_cart'] )
   total=total*100
   checkout_session = stripe.checkout.Session.create(
        line_items=[
            {
           
                'price_data': {
                    'product_data': {
                        'name': 'Total ',
                    },
                    'unit_amount': total ,
                    'currency': 'eur',
                },
                'quantity': 1,
            },
        ],
        payment_method_types=['card'],
        mode='payment',
        success_url=request.host_url + 'order/success',
        cancel_url=request.host_url + 'order/cancel',
    )
   order['payment'] = insert_payment()
   Address_Shipping.insert_address(order['address'])
   invoice = create_invoice()
   return redirect(checkout_session.url)

@checkout_bp.route('/order/success')
def success():
    try:
      Payment.update_status_db(order['payment'] ,"success")
      Invoice.update_status_db(order['invoice'],"success")
      session.clear()
      return render_template('success.html',invoice = order['invoice'])
    except Exception as e:
       print(e)


@checkout_bp.route('/order/cancel')
def cancel():
    Payment.update_status_db(order['payment'] ,"cancel")
    Invoice.update_status_db(order['invoice'],'cancel')
    return render_template('cancel.html', invoice = order['invoice'])

def insert_payment():
   amount = session['total_cart']
   type ='card'
   status ='pending'
   payment = Payment(amount,status,type)
   Payment.insert_payment_db(payment)
   return payment

def create_invoice():
   amount = session['total_cart']
   order_number = str(uuid.uuid4())
   id_user = current_user.get_id()
   invoice=Invoice(order_number,amount,id_user)
   is_insert = Invoice.insert_invoice_db(invoice)
   order['invoice'] = invoice
   if is_insert:
      current_user.invoices.append(invoice)
      insert_items_order()
      create_invoice_details(order['payment'], order['address'],invoice)

   return invoice

   
   
def insert_items_order():
   invoice = Invoice.get_invoice_by_number(order['invoice'])
   try:
    for key, value in session['shopping_cart'].items():
      id_product=key
      quantity=session['shopping_cart'][key]['quantity']
      item_order=Item_Order(quantity,id_product,invoice.id)
      item_order.insert_item_db()
      invoice.items.append(item_order)
   except Exception as e:
      print(e)
      



def create_invoice_details(payment,address,invoice):
   try:
      payment = Payment.get_payment_by_id(payment)
      address= Address_Shipping.get_address_by_id(address)
      invoice_details = Invoice_Details(invoice.id,payment.id,address.id)
      invoice_details.insert_invoice_details()
      payment.invoice_details.append(invoice_details)
      address.invoice_details.append(invoice_details)
      invoice.invoice_details.append(invoice_details)
   except Exception as e:
      print(e)

