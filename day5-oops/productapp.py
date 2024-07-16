class Product:
    mname='wipro'   #class variable 
    #constructor
    def __init__(self,id,name,price):
        self.id=id
        self.name=name
        self.price=price
    def disp(self):
        city='hyd'  #local
        print(self.id,self.name,self.price)
        print(Product.mname)
        print(city)
    def show():
        print(Product.mname)
p=Product(19,'bag',900)
p.disp()
p1=Product(20,'box',800)
p1.disp()
print(Product.mname)

    