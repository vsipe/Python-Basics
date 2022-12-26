class Item:
    pay_rate = 0.8 #the pay rate after 20% discount
    def __init__(self, name: str, price: float, quantity = 0):
        # Run validations to the received arguments
        assert price >= 0, f'Price {price} is not greater than or equal to zero!'
        assert quantity >= 0, f'Quantity {quantity} is not greater than or equal to zero'

        # assign to self object
        self.name = name 
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self): 
        return self.price * self.quantity 

    def apply_discount(self):
        self.price = self.price * self.pay_rate 
        #changed the Item.pay_rate to self.pay_rate, b/c that way it will use the .3 discount defined at the instance level 
        #from the .2 discount that we used earlier. 

item1 = Item('Phone', 100, 2)
item1.apply_discount()
print('This should give a 20% discount to 80 from 100:')
print(item1.price) 


item2 = Item('Laptop', 1000, 3)
item2.pay_rate = 0.7 #this will use pay_rate at the instance level, even though it isn't defined there. 
item2.apply_discount()
print('This should give a 30% discount to 700 from 1000:')
print(item2.price)
