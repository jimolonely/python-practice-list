#-*-codinf:utf-8-*-

class Product(object):
    
    def __init__(self,id,name,num,price):
        self.id = id
        self.name = str(name)
        self.num = num
        self.price = float(price)

    def __str__(self):
        return '[id='+str(self.id)+',name='+self.name+',num='+str(self.num)+',price='+str(self.price)+']'

class Store(object):
    
    def __init__(self):
        self.total = 0
        self.products = []

    def add(self,p):
        self.total += p.num * p.price
        self.products.append(p)

    def show(self):
        print('Total is: '+str(self.total))
        if type(apple) is Product:
            for p in self.products:
                print(p)
    
'''
test
'''
if __name__=='__main__':
    apple = Product(1,'apple',10,10.5)
    orange = Product(2,'orange',100,2.5)
    dog = Product(3,'dog',5,100.5)

    store = Store()
    store.add(apple)
    store.add(orange)
    store.add(dog)

    store.show()

