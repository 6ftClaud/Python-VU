# Sukuriama Customer klase
class Customer:

    # Sukuriamas klases Customer kintamasis "identifier"
    identifier = 0

    # Sukuriant klases objekta issaukiamas konstruktorius, kuris priima "name" kintamaji ir prekiu sarasa, kuris susideda is Item objektu
    def __init__(self, name, cart):
        self.__name = name
        # Klases Customer identifikatorius padidinamas vienetu kai sukuriamas naujas objektas
        Customer.identifier += 1
        """
        Klases Customer Objekto identifikatorius yra lygus klases Customer identifikatoriui.
        Taip issaugomas tikslus Objekto identifikatorius
        """
        self.identifier = Customer.identifier
        # Inicializuojamas krepselis
        self.init_cart(cart)

    # metodas get_identifier grazina Objekto identifikatoriu
    @property
    def get_identifier(self):
        return str(self.identifier)

    # metodas full_info grazina Objekto identifikatoriu ir varda
    @property
    def full_info(self):
        return str(self.identifier) + " " + self.__name

    # Objektams, esanciams sarase issaukiamas full_info metodas ir informacija surasoma i krepselio sarasa
    def init_cart(self, cart):
        items = []
        for item in cart:
            items.append(item.full_info())
        self.items = items

    # Prie krepselio saraso pridedama preke
    def add_item(self, item):
        self.items.append(item.full_info())

    # Is krepselio istrinama preke
    def remove_item(self, index):
        try:
            self.items.pop(index)
        # Jei preke su duotu indeksu neegzistuoja, apie tai pranesama
        except IndexError:
            print("Prekės su duotu indeksu nėra.")

    # Parodomas visas sarasas
    def get_items(self):
        print(self.items)

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

    # Prie Item klases full_info metodo pridedamas "Gerimas" string
    def full_info(self):
        return "Gėrimas" + " " + Item.full_info(self)


# Testavimas
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
