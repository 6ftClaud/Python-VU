class Item:

    def __init__(self, name, quantity=1, price=10):
        self.name = name
        self.quantity = quantity
        self.price = price

    def get_total_price(self):
        return (self.quantity * self.price)

    def full_info(self):
        return self.name + " " + str(self.price) + " " + str(self.quantity) + " " + str((self.quantity * self.price))

    def to_dict(self):
        dict = {
            "name": self.name,
            "quantity": self.quantity,
            "price": self.price,
            "total_price": self.get_total_price()
        }
        return dict


i1 = Item("Morkos")
i2 = Item("Pienas", 2, 1.5)
i3 = Item("Batonas", price=0.5)

print(i1.full_info())
print(i2.full_info())
print(i3.full_info())

print(i1.to_dict())
print(i2.to_dict())
print(i3.to_dict())
