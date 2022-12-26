import csv #need to import the csv

class Item:
    pay_rate = 0.8 

    all = [] #all list will add all objects that we have to a list 
    def __init__(self, name: str, price: float, quantity = 0):
        # run validations to the received arguments
        assert price >= 0, f'Price {price} is not greater than or equal to zero!'
        assert quantity >= 0, f'Quantity {quantity} is not greater than or equal to zero'
        
        # assign to self object
        self.name = name 
        self.price = price
        self.quantity = quantity

        #Actions to execute
        Item.all.append(self)

    def calculate_total_price(self): 
        return self.price * self.quantity 

    def apply_discount(self):
        self.price = self.price * self.pay_rate 

    @classmethod 
    def instantiate_from_csv(cls): #need to pass through a parameter again, but we want to stay away from calling it 'self' since that is for a different method.
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f) #will read this as a list of dictionaries
            items = list(reader) #set up this file
        
        for item in items:
            # **Need to make sure whenever you set up the .csv file that there are no spaces in between the files.**
            # ** Else you will get errors like this -> ValueError: invalid literal for int() with base 10: 'None'
            Item(
                name = item.get('name'),
                price = float(item.get('price')), #converts the price columns to a float
                quantity = float(item.get('quantity')), #converts the quantity columns to a float
           )


    def __repr__(self): #so that we can get a much cleaner & easier to read list for what's in the Item class. 
        # returns [Item("Phone", 100, 2), Item("Laptop", 1000, 3), Item("Cable", 10, 5), Item("Mouse", 50, 5), Item("Keyboard", 75, 5)]
        return f'Item("{self.name}", {self.price}, {self.quantity})'

Item.instantiate_from_csv()
print(Item.all)

phone1 = Item('jsPhonev10', 500, 5)
phone2 = Item('jsPhonev20', 700, 5)
