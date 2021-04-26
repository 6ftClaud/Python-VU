# Sukuriama Item klase
class Item:

    # Issaukiant klases konstruktoriu priimami trys kintamieji skirti prekei
    def __init__(self, name, quantity=1, price=10):
        self.name = name
        self.quantity = quantity
        self.price = price

    # metodas full_info grazina visa prekes informacija
    def full_info(self):
        return self.name + " " + str(self.price) + " " + str(self.quantity) + " " + str(self.get_total_price())

    # metodas get_total_price grazina prekes kaina
    def get_total_price(self):
        return (self.quantity * self.price)

    # Sukurus prekes "Dictionary", jis grazinamas
    def to_dict(self):
        dict = {
            "name": self.name,
            "quantity": self.quantity,
            "price": self.price,
            "total_price": self.get_total_price()
        }
        return dict


# Sukurta Food klase paveldi visus Item metodus
class Food(Item):

    def __init__(self, name, quantity=1, price=10):
        Item.__init__(self, name, quantity, price)

    # Prie Item klases full_info metodo pridedamas "Maistas" string
    def full_info(self):
        return "Maistas" + " " + Item.full_info(self)


# Sukurta Drink klase paveldi visus Item metodus
class Drink(Item):

    def __init__(self, name, quantity=1, price=10):
        Item.__init__(self, name, quantity, price)

    # Prie Item klases full_info metodo pridedamas "Gerimas" string
    def full_info(self):
        return "Gėrimas" + " " + Item.full_info(self)
