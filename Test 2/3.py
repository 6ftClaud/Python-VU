class Item:

    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def full_info(self):
        return self.name + " " + str(self.price) + " " + str(self.quantity) + " " + str(self.get_total_price())

    def get_total_price(self):
        return (self.quantity * self.price)


class Food(Item):
    def __init__(self, name, quantity, price):
        Item.__init__(self, name, quantity, price)

    def full_info(self):
        return "Maistas" + " " + Item.full_info(self)


class Drink(Item):
    def __init__(self, name, quantity, price):
        Item.__init__(self, name, quantity, price)

    def full_info(self):
        return "Gėrimas" + " " + Item.full_info(self)


f1 = Food("Batonas", 2, 1.3)
f2 = Food("Sviestas", 1, 1.3)

d1 = Drink("CocaCola", 3, 1.7)
d2 = Drink("Sprite", 2, 1.7)

print(f1.full_info())
print(f2.full_info())
print(d1.full_info())
print(d2.full_info())
