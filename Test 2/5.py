# Importuojama json biblioteka
import json

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
        self.cart = cart
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

    # Eksportuojama Customer klases "name" ir "identifier" kintamieji kartu su krepseliu
    def export_to_json(self, path):
        # Sukuriamas prekiu sarasas
        items = []
        # Visos prekes krepselyje pridedamos prie saraso
        for item in self.cart:
            items.append(item.to_dict())
        # Sukuriamas "data" dictionary
        data = {
            "name": self.__name,
            "identifier": self.get_identifier,
            "items": items
        }
        print(data)
        # "data" dictionary irasomas i .json file su json.dump metodu
        with open(path, "w", encoding="utf8") as file_obj:
            json.dump(data, file_obj, ensure_ascii=False, indent=4)

    """
    Perskaitomas .json failas ir su informacija sukuriamas naujas Customer objektas su
    "name", "identifier" kintamaisiais ir krepseliu
    """
    @classmethod
    def from_json(self, path):
        with open(path, "r", encoding="utf8") as file_obj:
            # json.load metodas perskaito informacija .json faile
            data = json.load(file_obj)
            # Sukuriamas naujas sarasas
            items = []
            # "for" ciklas kiekvienai prekei krepselyje
            for dictionary in data["items"]:
                # "dictionary" konvertuojamas i sarasa
                item = list(dictionary.values())
                # Is saraso reiksmiu sukuriamas naujas Item objektas
                item_object = Item(item[0], item[1], item[2])
                # Item objektas pridemamas prie "items" saraso
                items.append(item_object)
            # Grazinamas Customer klases objektas
            return Customer(data["name"], items)

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
print("Rašymas į failą:")
c1 = Customer("Jonas Jonaitis", [
              Food("Batonas", 2, 1.3), Drink("CocaCola", 3, 1.7)])
c1.export_to_json("customer.json")

print(f"\nFailo skaitymas:")
c1 = Customer.from_json("customer.json")
print(c1.full_info)
print(c1.get_items())
