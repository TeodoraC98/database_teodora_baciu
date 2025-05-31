
from sqlalchemy import Column, Integer, String, DateTime, Text,Float, ForeignKey
from sqlalchemy.orm import relationship
from app.models.orders import Item_Order

from app.database import Base, db_session
    
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
    
    
    # @validates('quantity')
    # def check_quantity(self, key, product_quantity):
    #     if product_quantity < 0:
    #         raise ValueError('Product quantity cannot be less than 0')
    #     return product_quantity
      
def insert_list_product(list):
    db_session.add_all(list)
    db_session.commit()
    return True

# creating instance of product for sholder bags
pr_sh_1=Product("Ali",100,"Lorem ipsum dolor sit amet consectetur adipisicing elit",85,'images/model_sh_ali.jpg')
pr_sh_2=Product("Amy",160,"Lorem ipsum dolor sit amet consectetur adipisicing elit",105,'images/model_sh_amy.jpg')
pr_sh_3=Product("Mara",430,"Lorem ipsum dolor sit amet consectetur adipisicing elit",125,'images/model_sh_mara.jpg')
pr_sh_4=Product("Diana",100,"Lorem ipsum dolor sit amet consectetur adipisicing elit",115,'images/model_sh_diana.jpg')
pr_sh_5=Product("Emily",100,"Lorem ipsum dolor sit amet consectetur adipisicing elit",90,'images/model_sh_emily.jpg')
pr_sh_6=Product("Emma",100,"Lorem ipsum dolor sit amet consectetur adipisicing elit",110,'images/model_sh_emma.jpg')
pr_sh_7=Product("Evelin",100,"Lorem ipsum dolor sit amet consectetur adipisicing elit",130,'images/model_sh_evelin.jpg')
pr_sh_8=Product("Mona",100,"Lorem ipsum dolor sit amet consectetur adipisicing elit",200,'images/model_sh_mona.jpg')
pr_sh_9=Product("Ruth",100,"Lorem ipsum dolor sit amet consectetur adipisicing elit",210,'images/model_sh_ruth.jpg')
pr_sh_10=Product("Theo",100,"Lorem ipsum dolor sit amet consectetur adipisicing elit",195,'images/model_sh_theo.jpg')
pr_sh_11=Product("Tiffany",100,"Lorem ipsum dolor sit amet consectetur adipisicing elit",285,'images/model_sh_tiffany.jpg')

list_sholder_bgs=[pr_sh_1,pr_sh_2,pr_sh_3,pr_sh_4,pr_sh_5,pr_sh_6,pr_sh_7,pr_sh_8,pr_sh_9,pr_sh_10,pr_sh_11]
# creating instance of product for handle bags
pr_hd_1=Product("Ciara",100,"Lorem ipsum dolor sit amet consectetur adipisicing elit",85,'images/model_hd_ciara.jpg')
pr_hd_2=Product("Elena",100,"Lorem ipsum dolor sit amet consectetur adipisicing elit",125,'images/model_hd_elena.jpg')
pr_hd_3=Product("Cora",100,"Lorem ipsum dolor sit amet consectetur adipisicing elit",235,'images/model_hd_cora.jpg')
pr_hd_4=Product("Martina",100,"Lorem ipsum dolor sit amet consectetur adipisicing elit",115,'images/model_hd_martina.jpg')
pr_hd_5=Product("Rose",100,"Lorem ipsum dolor sit amet consectetur adipisicing elit",145,'images/model_hd_rose.jpg')
pr_hd_6=Product("Silvia",100,"Lorem ipsum dolor sit amet consectetur adipisicing elit",85,'images/model_hd_silvia.jpg')
list_handle_bgs=[pr_hd_1,pr_hd_2,pr_hd_3,pr_hd_4,pr_hd_5,pr_hd_6]

# creating instance of product for  bags clutch
pr_ch_1=Product("Aurora",100,"Lorem ipsum dolor sit amet consectetur adipisicing elit",125,'images/model_ch_aurora.jpg')
pr_ch_2=Product("Mary",100,"Lorem ipsum dolor sit amet consectetur adipisicing elit",140,'images/model_ch_mary.jpg')
pr_ch_3=Product("Mina",100,"Lorem ipsum dolor sit amet consectetur adipisicing elit",155,'images/model_ch_mina.jpg')
pr_ch_4=Product("Monica",100,"Lorem ipsum dolor sit amet consectetur adipisicing elit",200,'images/model_ch_monica.jpg')
pr_ch_5=Product("Rachel",100,"Lorem ipsum dolor sit amet consectetur adipisicing elit",200,'images/model_ch_rachel.jpg')
list_clutch_bgs=[pr_ch_1,pr_ch_2,pr_ch_3,pr_ch_4,pr_ch_5]

# creating instance of category for each type of bag
category_Product1=Category_Product("handle"," Lorem ipsum dolor sit amet consectetur adipisicing elit. Velit mollitia voluptas consequatur " \
"voluptatibus a architecto, aut delectus ducimus magnam corporis impedit eum debitis doloremque odio",list_handle_bgs)
category_Product2=Category_Product("clutch"," Lorem ipsum dolor sit amet consectetur adipisicing elit. " \
"Velit mollitia voluptas consequatur voluptatibus a architecto, aut delectus ducimus magnam corporis impedit eum debitis doloremque odio",list_clutch_bgs)
category_Product3=Category_Product("sholder"," Lorem ipsum dolor sit amet consectetur adipisicing elit." \
" Velit mollitia voluptas consequatur voluptatibus a architecto, aut delectus ducimus magnam corporis impedit eum debitis doloremque odio",list_sholder_bgs)

list_category=[category_Product1,category_Product2, category_Product3]

def insert_category():
    for category in list_category:
        stm=category.register_category()
        if stm:
            stm_pr=insert_list_product(category.products)
 




