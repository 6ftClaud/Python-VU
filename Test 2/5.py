import json


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
        self.cart = cart
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

    def export_to_json(self, path):
        items = []
        for item in self.cart:
            items.append(item.to_dict())
        data = {
            "name": self.__name,
            "identifier": self.get_identifier,
            "items": items
        }
        print(data)
        with open(path, "w", encoding="utf8") as file_obj:
            json.dump(data, file_obj, ensure_ascii=False, indent=4)

    @classmethod
    def from_json(self, path):
        with open(path, "r", encoding="utf8") as file_obj:
            data = json.load(file_obj)
            items = []
            for dictionary in data["items"]:
                item = list(dictionary.values())
                item_object = Item(item[0], item[1], item[2])
                items.append(item_object)
            return Customer(data["name"], items)

class Item:

    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def full_info(self):
        return self.name + " " + str(self.price) + " " + str(self.quantity) + " " + str(self.get_total_price())

    def get_total_price(self):
        return (self.quantity * self.price)

    def to_dict(self):
        dict = {
            "name": self.name,
            "quantity": self.quantity,
            "price": self.price,
            "total_price": self.get_total_price()
        }
        return dict


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


print("Rašymas į failą:")
c1 = Customer("Jonas Jonaitis", [
              Food("Batonas", 2, 1.3), Drink("CocaCola", 3, 1.7)])
c1.export_to_json("customer.json")

print(f"\nFailo skaitymas:")
c1 = Customer.from_json("customer.json")
print(c1.full_info)
print(c1.get_items())
