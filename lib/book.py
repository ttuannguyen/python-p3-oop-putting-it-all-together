#!/usr/bin/env python3

class Book:
    
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count
    
    def get_page_count(self):
        print("Retrieving page count.")
        return self._page_count

    def set_page_count(self, page_count):
        if isinstance(page_count, int):
            print(f"Setting page count to { page_count }")
            self._page_count = page_count
        else:
            print("page_count must be an integer")
    
    page_count = property(get_page_count, set_page_count)

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")


book = Book("Awesome", 100)
# book.turn_page()
        

