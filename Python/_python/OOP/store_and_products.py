class Store:
    def __init__(self, name, products_list=[]):
        self.store_name = name
        self.products_list = products_list

    def add_product(self, new_product):
        self.new_product = new_product
        self.products_list.append(new_product)
        return self

    def sell_product(self, id):
        print(self.products_list[id])
        self.products_list.pop(id)
        return self
class Product:
    def __init__(self, name, price, category):
        self.product_name = name
        self.price = price
        self.category = category
        self.product = [name, price, category]

    def update_price(self, percent_changed, is_increased):
        if is_increased == True:
            self.price += self.price * percent_changed
        else:
            self.price -= self.price / percent_changed
        return self

    def print_info(self):
        print(f"Product Name: {self.product_name}; Product Category: {self.category}; Product Price: ${self.price}")
        return self

store1 = Store("My First Store")
product1 = Product("Bang", 3.50, "Energy Drinks")
product2 = Product("Cliff Builder", 2.50, "Protein Bars")
product3 = Product("Lifeblood", 15.99, "Multivitamins")

store1.add_product(product1.product).add_product(product2.product).add_product(product3.product)

print(store1.products_list)
store1.sell_product(0)
print(store1.products_list)