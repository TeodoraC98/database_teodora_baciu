from sqlalchemy import Column, Integer, Float,String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base, db_session
from datetime import datetime,timezone
from app.models.payments import Payment
from app.models.address import Address_Shipping

# Item_Order instances represent the item of each product in the cart
# the relationship between Product and Item_Order  is one-to-one 
# the Item_Order is referencing the Product through the  foreign key id_product

# the relationship between Invoice and Item_Order  is one-to-many 
# the Item_Order is referencing the Invoice through the  foreign key id_order
class Item_Order(Base):
    __tablename__='items'
    id=Column(Integer,primary_key=True, autoincrement=True)
    quantity=Column(Integer,nullable=False)
    id_product=Column(Integer,ForeignKey('products.id'),nullable=False)
    id_order=Column(Integer,ForeignKey('invoices.id'),nullable=False)
    product=relationship("Product", back_populates="item_cart")
    order=relationship("Invoice", back_populates="items")

    def to_dict(self):
        return{
            "id":self.id,
            "quantit":self.quantity,
            "id_product":self.id_product,
            "id_order":self.id_order,
            "product":{
                'id':self.product.id,
                'name':self.product.name,
                'quantity':self.product.quantity,
                'description':self.product.description,
                'price':self.product.price,
                'img_url':self.product.img_url
            }
        }
    def __init__(self,quantity,id_product,id_order):
        self.quantity=quantity
        self.id_product=id_product
        self.id_order=id_order

    def insert_item_db(self):
        db_session.add(self)
        db_session.commit()
        return True


class Invoice(Base):
    __tablename__='invoices'
    id = Column(Integer,primary_key=True,nullable=False, autoincrement=True)
    order_number = Column(String(230),nullable=False,unique=True)
    date = Column(DateTime, nullable=False, default= datetime.now(timezone.utc))
    status=Column(String(20),nullable=False,default='pending')
    amount = Column(Float,default=0.0,nullable=False)
    id_user = Column(Integer,ForeignKey('users.id'),nullable=False)
    items = relationship("Item_Order",back_populates="order",cascade="all, delete")
    invoice_details=relationship("Invoice_Details",back_populates='invoice')
    user=relationship("User",back_populates='invoices')

    def __init__(self, order_number,amount,id_user):
        self.order_number=order_number
        self.amount=amount
        self.id_user=id_user

    def to_dict(self):
        return{
            "id":self.id,
            "order_number":self.order_number,
            "date":self.date,
            "amount":self.amount,
            "id_user":self.id_user,
            "items":[{
                "id":item.id,
                "quantit":item.quantity,
                "id_product":item.id_product,
                "id_order":item.id_order
             }
            for item in self.items]
        }
     
    def insert_invoice_db(self):
        try:
          db_session.add(self)
          db_session.commit()
          return True
        except Exception as e:
            print(e)
       
    
    def update_status_db(self,status):
        try:
          update=Invoice.query.filter(Invoice.id==self.id).update({'status':status})
          db_session.commit()
        except Exception as e:
            print(e)

    def get_list_invoice_by_user(id_user):
        try:
         list_invoice = Invoice.query.filter(Invoice.id_user == id_user).all()
         return list_invoice
        except Exception as e:
            print(e)
    # each invoice has an unique number, that can be used for making a select
    def get_invoice_by_number(self):
        try:
         invoice = Invoice.query.filter(Invoice.order_number == self.order_number).first()
         return invoice
        except Exception as e:
            print(e)
    
    # I use the Invoice_Details class to make it easier to access data such as: payment, address and invoice
# the relationship between Invoice_Details and Invoice  is one-to-one 
# the Invoice_Details is referencing the Invoice through the  foreign key id_invoice

# the relationship between Invoice_Details and Payment  is one-to-one 
# the Invoice_Details is referencing the Payment through the  foreign key id_paymemnt

# the relationship between Invoice_Details and Address  is one-to-one 
# the Invoice_Details is referencing the Address through the  foreign key id_address

class Invoice_Details(Base):
    __tablename__='invoice_details'
    id=Column(Integer,primary_key=True,nullable=False, autoincrement=True)
    id_invoice=Column(Integer,ForeignKey('invoices.id'),nullable=False)
    id_payment=Column(Integer,ForeignKey('payments.id'),nullable=False)
    id_address=Column(Integer,ForeignKey('addresses.id'),nullable=False)
    invoice=relationship("Invoice",back_populates='invoice_details')
    payment=relationship("Payment",back_populates='invoice_details')
    address=relationship("Address_Shipping",back_populates='invoice_details')
     
    def __init__(self,id_invoice,id_payment,id_address):
        self.id_invoice=id_invoice
        self.id_payment=id_payment
        self.id_address=id_address

    def to_dict(self):
        return{
            "id":self.id,
            "id_invoice":self.id_invoice,
            "id_payment":self.id_payment,
            "id_address":self.id_address,
            "address":{
                "id_address":self.address.id,
                "street":self.address.street,
                "apartament":self.address.apartment,
                "city":self.address.city,
                "county":self.address.county,
                "postcode":self.address.postcode,
                "estimate_arrival":self.address.estimate_arrival
             },
             "payment":{
                "id_payment":self.payment.id,
                "amount":self.payment.amount,
                "date":self.payment.date,
                "status":self.payment.status,
                "type":self.payment.type
             }   
        }
    def get_invoice_details_by_id(id):
        try:
         invoice_delails = Invoice_Details.query.filter(Invoice_Details.id == id).first()
         return invoice_delails
        except Exception as e:
            print(e)

    def get_invoice_details_by_id_invoice(id_invoice):
        try:
         invoice_delails = Invoice_Details.query.filter(Invoice_Details.id_invoice == id_invoice).first()
         return invoice_delails
        except Exception as e:
            print(e)
            
    

    
    def insert_invoice_details(self):
        try:
         db_session.add(self)
         db_session.commit()
         return True
        except Exception as e:
            print(e)
            
    