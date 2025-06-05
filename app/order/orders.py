from flask import session, Blueprint,render_template,redirect,url_for,request
from sqlalchemy import select
from app.models.orders import Invoice,Invoice_Details
from app.database import db_session
order_bp = Blueprint('orders',__name__,template_folder='templates/orders')
# the user acces the information(address,payment,items) about the order
# from invoice ->  can access items
# invoice_details -> can access payment and address
# first the user, select an invoice from the list of the invoices 
# then based on the invoice id is selected the invoice_details 
@order_bp.route('/invoice/<string:order_number>')
def get_invoice_by_order_number(order_number):
    invoice_stm = select(Invoice).where(Invoice.order_number == order_number)
    invoice = db_session.scalars(invoice_stm).first()
    invoice_details=Invoice_Details.get_invoice_details_by_id_invoice(invoice.id)
    return render_template("invoice.html",invoice = invoice,invoice_details = invoice_details)