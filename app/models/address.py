from sqlalchemy import Column, Integer,String,Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base, db_session
from datetime import datetime,timezone,timedelta

class Address_Shipping(Base):
    __tablename__='addresses'
    id=Column(Integer,primary_key=True, autoincrement=True)
    street=Column(String(50), nullable=False)
    apartment=Column(String(25),nullable=True, default='NULL')
    city=Column(String(50),nullable=False)
    county=Column(String(50),nullable=False)
    postcode=Column(String(7),nullable=False)
    cost=Column(Float,default=00.00)
    estimate_arrival = Column(DateTime, default= datetime.now(timezone.utc))
    invoice_details=relationship('Invoice_Details',back_populates='address',lazy='subquery')
    def __init__(self,street,city,county,postcode,estimate_arrival,cost):
        self.street = street
        self.city = city
        self.county = county
        self.postcode = postcode
        self.estimate_arrival = estimate_arrival
        self.cost = cost
    
    def to_dict(self):
        return{
            "id_address":self.id,
            "street":self.street,
            "apartament":self.apartment,
            "city":self.city,
            "county":self.county,
            "postcode":self.postcode,
            "estimate_arrival":self.estimate_arrival
        }
             
    def insert_address(self):
        try:
           db_session.add(self)
           db_session.commit()
           return self.id
        except Exception as e:
            print(e)
    

    
    def get_address_by_id(self):
        try:
          address = Address_Shipping.query.filter(Address_Shipping.id==self.id).first()
          return address
        except Exception as e:
            print(e)
    
# Delivery_Type defined the 3 instance of delivery options: free, standard and express
# each option has a different cost and the estimated delivery date is different
# I'm using Delivery_Type class to set the cost, and estimate_delivery based on user's choice
class Delivery_Type:
    def __init__(self,cost):
       self.cost=cost
       self.estimate_arrival=datetime.now(timezone.utc)

   # the function determines the estimated delivery day of the order based on the type of the delivery
    def set_estimate_delivery(self,delivery_time):
        current_date = datetime.now(timezone.utc)
        # the delivery_time is different depending  on the  Delivery_Type
        estimate_devilery = current_date  + timedelta(delivery_time)
        # if the estimate_devilery is the week day, then is set as estimate_devilery
        if estimate_devilery.weekday() <=4:
           self.estimate_arrival=estimate_devilery
        elif estimate_devilery.weekday() == 5:
        #    if estimate_devilery is a Friday, the estimate_devilery is set to be the next Monday
           estimate_devilery = estimate_devilery  + timedelta(2)
           self.estimate_arrival=estimate_devilery
        else:
           estimate_devilery = estimate_devilery  + timedelta(1)
           self.estimate_arrival=estimate_devilery
    
    def __str__(self):
        return f" Delivery cost is{self.cost} and date {self.estimate_arrival}"

free = Delivery_Type(0)
free.set_estimate_delivery(10)
standard = Delivery_Type(10)
standard.set_estimate_delivery(5)
express = Delivery_Type(20)
express.set_estimate_delivery(1)
 
delivery_types={
  "free":free,
  "standard":standard,
  "express":express
}