class Item:
    def __init__(self, name, price, quantity = 0):
        # say what you want to be in the method in this __init__ constructor
        #replaces the need to initiate a price & quantity for each one, ie no need for item1.price = 100, etc. 
        # we can just pass them into the method using item1 = Item('Phone', 100, 5)
        self.name = name 
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self): #can delete x & y now since self.price & self.quantity are entered here. 
        return self.price * self.quantity #need the self.price so that the method knows that you're looking locally instead of globally




item1 = Item('Phone', 100, 1)


item2 = Item('Laptop', 1000, 3)

#item2.has_numpad = False #can add more attributes to the method even though they aren't substantiated in the constructor (__init__)
print(item1.calculate_total_price())
print(item2.calculate_total_price())

