import random
class Product:
    def __init__(self, name, price, category):
        self.product_name = name
        self.price = price
        self.category = category
        self.uni_id = random.getrandbits(32)

    def update_price(self, percent_changed, is_increased):
        if is_increased == True:
            self.price += self.price * (percent_changed / 100)
            print(f"Looks like the {self.product_name} price increased, which is now ${self.price}")
        else:
            self.price -= self.price * (percent_changed / 100)
            print(f"Looks like the {self.product_name} price just decreased! It's now ${self.price}")
        return self

    def print_info(self):
        print(f"Product Name: {self.product_name}; Product Category: {self.category}; Product Price: ${self.price}")
        return self