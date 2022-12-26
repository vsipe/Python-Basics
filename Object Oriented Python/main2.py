class Item:
    def __init__(self, name, price, quantity):
        # say what you want to be in the method in this __init__ constructor
        #replaces the need to initiate a price & quantity for each one, ie no need for item1.price = 100, etc. 
        # we can just pass them into the method using item1 = Item('Phone', 100, 5), see below.
        self.name = name 
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self, x, y):
        #python passes the object itself when you do something with it. 
        #so the (self) is taking item1 and entering it into the method.
        # if you don't have it you get this error - TypeError: Item.calculate_total_price() takes 0 positional arguments but 1 was given, 
        # meaning that you need some parameter entered in the method.
        return x * y 




item1 = Item('Phone', 100, 5)
#these are now attributes of item1 instead of their own variables

#print(item1.calculate_total_price(item1.price, item1.quantity)) 

item2 = Item('Laptop', 1000, 3)
#these are now attributes of item1 instead of their own variables

#print(item2.calculate_total_price(item2.price, item2.quantity))

print(item1.name)
print(item2.name)
print(item1.price)
print(item2.price)
print(item1.quantity)
print(item2.quantity)