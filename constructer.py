class Item:
    def calculate_total_price(self,x,y):
        return x*y
item1 = Item()
item_price = 2300
item_quantity = 45
print(item1.calculate_total_price(item_price,item_quantity))