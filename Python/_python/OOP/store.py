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