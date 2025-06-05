from datetime import datetime,timezone
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy import Column, Integer,String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base, db_session
    
    # the relationship between User and Invoice is one-to-many 
    # the Invoice is referencing the User through the  foreign key id_user
class User(UserMixin, Base):
    __tablename__= 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name=Column(String(30),nullable=False)
    surname=Column(String(30),nullable=False)
    contact_nr=Column(Integer,nullable=False)
    email=Column(String(125),nullable=False, unique=True)
    password_hash=Column(String(230),nullable=False)
    created_at = Column(DateTime, default= datetime.now(timezone.utc))
    invoices=relationship("Invoice",back_populates="user")
    
    def __init__(self,first_name,surname,contact_nr, email):
        self.first_name=first_name
        self.surname=surname
        self.contact_nr=contact_nr   
        self.email=email
    

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __str__(self):
        return f"{self.email} and {self.first_name} "

    def __repl__(self):
        return f"{self.first_name}"
 
    def register_user(self):
        db_user = User.query.filter(User.email==self.email).all()
        if not db_user:
            db_session.add(self)
            db_session.commit()
            return True
        else:
            return False
        
    def get_by_email(email):
        user=User.query.filter(User.email==email).first()
        return user

  
    