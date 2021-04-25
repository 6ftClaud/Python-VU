class Customer:
    identifier = 0

    def __init__(self, name):
        self.__name = name
        Customer.identifier += 1
        self.identifier = Customer.identifier

    @property
    def get_identifier(self):
        return str(self.identifier)

    @property
    def full_info(self):
        return str(self.identifier) + " " + self.__name


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
