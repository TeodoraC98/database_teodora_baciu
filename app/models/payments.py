from sqlalchemy import Column, Integer, Float,String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base, db_session
from datetime import datetime,timezone

class Payment(Base):
    __tablename__='payments'
    id=Column(Integer,primary_key=True,autoincrement=True)
    amount=Column(Float,nullable=False, default=0.0)
    date=Column(DateTime, nullable=False, default= datetime.now(timezone.utc))
    status=Column(String(20),nullable=False,default='pending')
    type=Column(String(20),nullable=False)
    invoice_details=relationship('Invoice_Details',back_populates='payment',uselist=True)

    def __init__(self,amount,status,type):
        self.amount=amount
        self.status=status
        self.type=type
        self.date=datetime.now(timezone.utc)

    def get_payment_by_id(self):
        try:
          payment = Payment.query.filter(Payment.id  == self.id).first()
          return payment
        except Exception as e:
            print(e)
   
    def insert_payment_db(self):
        db_session.add(self)
        db_session.commit()
        return self.id
    
    def update_status_db(self,status):
        update=Payment.query.filter(Payment.id==self.id).update({'status':status})
        db_session.commit()
    
    