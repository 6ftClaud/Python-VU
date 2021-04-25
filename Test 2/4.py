class Customer:

    identifier = 0

    def __init__(self, name, cart):
        self.__name = name
        Customer.identifier += 1
        self.identifier = Customer.identifier
        self.init_cart(cart)

    @property
    def get_identifier(self):
        return str(self.identifier)

    @property
    def full_info(self):
        return str(self.identifier) + " " + self.__name

    def init_cart(self, cart):
        items = []
        for item in cart:
            items.append(item.full_info())
        self.items = items

    def add_item(self, item):
        self.items.append(item.full_info())

    def remove_item(self, index):
        try:
            self.items.pop(index)
        except IndexError:
            print("Prekės su duotu indeksu nėra.")

    def get_items(self):
        print(self.items)

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


c1 = Customer("Jonas Jonaitis", [
              Food("Batonas", 2, 1.3), Drink("CocaCola", 3, 1.7)])
c2 = Customer("Petras Petraitis", [
              Food("Sviestas", 1, 1.3), Drink("Sprite", 2, 1.7)])

print(c1.get_items())
print(c2.get_items())

c1.add_item(Drink("Fanta", 10, 1.7))
print(c1.get_items())

c2.remove_item(2)
c2.remove_item(1)
print(c2.get_items())
