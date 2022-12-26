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
        self.price = self.price * Item.pay_rate #need to look at pay rate in the class level, therefore we need the Item.pay_rate instead of just pay_rate

item1 = Item('Phone', 100, 2)

 
