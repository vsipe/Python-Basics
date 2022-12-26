from item import Item

class Keyboard(Item):
    pay_rate = 0.7
    def __init__(self, name: str, price: float, quantity = 0):
        # call to super function to have access to all attributes/methods (can access the Item methods of name, price & quantity)
        super().__init__(
            name, price, quantity
        )
