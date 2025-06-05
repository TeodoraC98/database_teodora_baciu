
from sqlalchemy import Column, Integer, String, DateTime, Text,Float, ForeignKey
from sqlalchemy.orm import relationship
from app.models.orders import Item_Order

from app.database import Base, db_session

    # the relationship between Category_Product and Product  is one-to-many
    # the Product is referencing the Category_product through the  foreign key id_category
class Category_Product(Base):
    __tablename__='category_product'

    id=Column(Integer,primary_key=True,autoincrement=True)
    category_name=Column(String(100), nullable=False,unique = True)
    description=Column(String(400), nullable=False)
    products= relationship("Product", back_populates="category", cascade="all, delete")

    def __init__(self, category_name, description,products):
        self.category_name = category_name
        self.description = description
        self.products=products

      
       
    def register_category(self):
        db_category = Category_Product.query.filter(Category_Product.category_name==self.category_name).all()
        if not db_category:
            db_session.add(self)
            db_session.commit()
            return True
        else:
            return False
    
    def to_dict(self):
        return{
            'id_category':self.id,
            'category_name':self.category_name,
            'products':[{
                'id':product.id,
                'name':product.name,
                'quantity':product.quantity,
                'description':product.description,
                'price':product.price,
                'img_url':product.img_url
            }
            for product in self.products
            ]
        }
        
    def get_category(category_name):
        category=Category_Product.query.filter(Category_Product.category_name == category_name).first()
        return category
    
    # the relationship between Product and ItemCart is one-to-one  
    # the ItemCart is referencing the Product through the  foreign key id_product

class Product(Base):
    __tablename__='products'
    id=Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String(100), nullable=False)
    quantity = Column(Integer, nullable=False)
    description=Column(Text, nullable=False)
    price = Column(Float, nullable=False, default=0.0)
    img_url=Column(String(100), nullable=False)
    id_category=Column(Integer, ForeignKey('category_product.id'), nullable=False)
    category = relationship("Category_Product",  back_populates="products")
    item_cart=relationship("Item_Order", back_populates="product")
    
    def __init__(self, name, quantity, description, price, img_url):
        self.name=name
        self.quantity=quantity
        self.description=description
        self.price=price
        self.img_url=img_url

    def to_dict(self):
        return{
         'id':self.id,
        'name':self.name,
        'quantity':self.quantity,
        'description':self.description,
        'price':self.price,
        'img_url':self.img_url
        }
    def get_product_by_id(id):
        try:
          product = Product.query.filter(Product.id==id).first()
          return product
        except Exception as e:
            print(e)
     
    def insert_product(self):
        db_session.add(self)
        db_session.commit()
        return True
    


