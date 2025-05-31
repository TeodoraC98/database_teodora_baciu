class ItemCart: 
    def __init__(self, id,name,quantity, price,total_price,img_url):
        self.id=id
        self.name=name
        self.quantity=quantity
        self.price=price
        self.total_price=total_price
        self.img_url=img_url
        
    def __str__(self):                            
     return f"{self.id}({self.name})"
    
    def jsonfy(self):
       return{
          'id':self.id,
          'name':self.name,
          'quantity':self.quantity,
          'price':self.price,
          'total_price':self.total_price,
          'img_url':self.img_url      
       }