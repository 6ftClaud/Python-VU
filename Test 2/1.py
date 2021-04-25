# Sukuriama Customer klase
class Customer:
    # Sukuriamas klases Customer kintamasis "identifier"
    identifier = 0

    # Sukuriant klases objekta issaukiamas konstruktorius kuris priima "name" kintamaji
    def __init__(self, name):
        # Sukuriamas privatus "name" kintamasis
        self.__name = name
        # Klases Customer identifikatorius padidinamas vienetu kai sukuriamas naujas objektas
        Customer.identifier += 1
        """
        Klases Customer Objekto identifikatorius yra lygus klases Customer identifikatoriui.
        Taip issaugomas tikslus Objekto identifikatorius
        """
        self.identifier = Customer.identifier

    # metodas get_identifier grazina Objekto identifikatoriu
    @property
    def get_identifier(self):
        return str(self.identifier)

    # metodas full_info grazina Objekto identifikatoriu ir varda
    @property
    def full_info(self):
        return str(self.identifier) + " " + self.__name


# Testavimas
c1 = Customer("Jonas Jonaitis")
c2 = Customer("Petras Petraitis")
c3 = Customer("Lukas Lukauskas")

print(Customer.identifier)

print(c1.get_identifier)
print(c2.get_identifier)
print(c3.get_identifier)

print(Customer.identifier)

print(c1.full_info)
print(c2.full_info)
print(c3.full_info)
