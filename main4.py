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



item1 = Item('Phone', 100, 2)
item2 = Item('Laptop', 1000, 3)

print("All of the attributes for the Class Level: ") #note how pay_rate is only included in the class level, and it isn't in the instance level? 
print(Item.__dict__)
print('\n')

print("All of the attributes for the instance Level: ") 
print(item1.__dict__)
print('\n')

# this will always give the same result. Python looks for the pay rate in the self.name section first, and then will look in the instance level 
# (outside of the __init__ method)
print(Item.pay_rate) 
print(item1.pay_rate) 
print(item2.pay_rate) 


