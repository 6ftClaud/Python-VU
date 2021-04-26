# Importuojama Item klase is item.py, reikalinga from_json metodui
from .item import Item

# Importuojama json biblioteka reikalinga from_json ir export_to_json metodams
import json

# Sukuriama Customer klase
class Customer:

    # Sukuriamas klases Customer kintamasis "identifier"
    identifier = 0

    # Sukuriant klases objekta issaukiamas konstruktorius, kuris priima "name" kintamaji ir prekiu sarasa, kuris susideda is Item objektu
    def __init__(self, name, cart=None):
        self.__name = name
        # Klases Customer identifikatorius padidinamas vienetu kai sukuriamas naujas objektas
        Customer.identifier += 1
        """
        Klases Customer Objekto identifikatorius yra lygus klases Customer identifikatoriui.
        Taip issaugomas tikslus Objekto identifikatorius
        """
        self.identifier = Customer.identifier
        # Jei klases konstruktoriui perduodamas krepselis, jis inicializuojamas
        if cart:
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
