#!/usr/bin/env python3

class Shoe:
    
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size

    
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if isinstance(size, int):
            print(f"Setting size to { size }")
            self._size = size
        else:
            print("size must be an integer")
    
    
    # def get_size(self):
    #     print("Retrieving size.")
    #     return self._size

    # def set_size(self, size):
    #     if isinstance(size, int):
    #         print(f"Setting size to { size }")
    #         self._size = size
    #     else:
    #         print("size must be an integer")
    
    # size = property(get_size, set_size)

    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")


shoe = Shoe("Nike", 7)
shoe.size = 8
shoe.size = "hello"
    