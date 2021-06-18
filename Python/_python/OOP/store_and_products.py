class Store:
    def __init__(self, name):
        self.store_name = name
        self.products_list = []

    def add_product(self, new_product):
        self.new_product = new_product
        self.products_list.append(new_product)
        return self

    def sell_product(self, id):
        removing = self.products_list[id]
        self.products_list.pop(id)
        print(f"You just sold the product: {removing.product_name}!")
        return self

    def inflation(self, percent_increase):
        for item in range(len(self.products_list)):
            self.products_list[item].update_price(percent_increase, True)
    
    def set_clearance(self, category, percent_discount):
        for ctg in range(len(self.products_list)):
            if self.products_list[ctg].category == category:
                self.products_list[ctg].update_price(percent_discount, False)
class Product:
    def __init__(self, name, price, category):
        self.product_name = name
        self.price = price
        self.category = category

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