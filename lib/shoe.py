#!/usr/bin/env python3

class Shoe:
    
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size

    def get_size(self):
        pass

    def set_size(self, size):
        pass
    
    size = property(get_size, set_size)


# shoe = Shoe("Nike", 7)
    