# when to use class methods and when to use static methods? 

class Item:
    @staticmethod
    def is_integer():
        '''
        This should do something that has a relationship with the class, but not something that must be unique per instance
        '''

    @classmethod
    def instantiate_from_something(cls):
        '''
        This should also do something that has a relationship with the class but usually, these are used to manipulate 
        different structures of data to instantiate objects, for example, when we're reading the .csv. basically something has to pass into it
        '''

item1 = Item()
item1.is_integer()
item1.instantiate_from_something()
