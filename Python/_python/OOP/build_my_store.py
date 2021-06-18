import store
import products

store1 = store.Store("My First Store")
product1 = products.Product("Bang", 3.50, "Energy Drinks")
product2 = products.Product("Cliff Builder", 2.50, "Protein Bars")
product3 = products.Product("Lifeblood", 15.99, "Multivitamins")

store1.add_product(product1).add_product(product2).add_product(product3)
product1.update_price(2, True)
store1.products_list[0].print_info()
store1.products_list[1].print_info()
store1.sell_product(1)
store1.inflation(5)
store1.set_clearance("Energy Drinks", 50)