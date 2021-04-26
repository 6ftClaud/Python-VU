from shop.customer import Customer
from shop.item import Food, Drink


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
