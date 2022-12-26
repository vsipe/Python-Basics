from phone import Phone
from keyboard import Keyboard

item1 = Keyboard('jscKeyboard', 1000, 3)
# 4 OOP concepts - 
#1. encapsulation - determine what information that you might not want the user to change
# z.b. we changed price to __price.


#2. Abstraction - we only want to show the user necessary information. we changed
# the item document to have the attributes connect, send, prepare_body, but don't want
# the user to need to mess with those.
item1.apply_discount()

print(item1.price)

#3. Inheritance - set things up so we can re-use code throughout all of our classes.
# we can access send_email() even though it's in the Item class. 

#4. polymorphism - many forms - can have different pay_rate for each different item, 
# we set phone's pay_rate to 0.5
# we created a new class that has a different pay_rate of 0.7

# this is what I learned from the attached youtube video: https://www.youtube.com/watch?v=Ej_02ICOIgs&t=6393s