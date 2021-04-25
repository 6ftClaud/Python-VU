# Sukuriama Item klase
class Item:

    # Issaukiant klases konstruktoriu priimami trys kintamieji skirti prekei
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    # metodas full_info grazina visa prekes informacija
    def full_info(self):
        return self.name + " " + str(self.price) + " " + str(self.quantity) + " " + str(self.get_total_price())

    # metodas get_total_price grazina prekes kaina
    def get_total_price(self):
        return (self.quantity * self.price)


# Sukurta Food klase paveldi visus Item metodus
class Food(Item):
    def __init__(self, name, quantity, price):
        Item.__init__(self, name, quantity, price)

    # Prie Item klases full_info metodo pridedamas "Maistas" string
    def full_info(self):
        return "Maistas" + " " + Item.full_info(self)


# Sukurta Drink klase paveldi visus Item metodus
class Drink(Item):
    def __init__(self, name, quantity, price):
        Item.__init__(self, name, quantity, price)

    # Prie Item klases full_info metodo pridedamas "Maistas" string
    def full_info(self):
        return "Gėrimas" + " " + Item.full_info(self)


# Testavimas
f1 = Food("Batonas", 2, 1.3)
f2 = Food("Sviestas", 1, 1.3)

d1 = Drink("CocaCola", 3, 1.7)
d2 = Drink("Sprite", 2, 1.7)

print(f1.full_info())
print(f2.full_info())
print(d1.full_info())
print(d2.full_info())
