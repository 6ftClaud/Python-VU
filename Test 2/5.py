from shop.customer import Customer
from shop.item import Food, Drink


# Testavimas
print("Rasymas i faila:")
c1 = Customer("Jonas Jonaitis", [
              Food("Batonas", 2, 1.3), Drink("CocaCola", 3, 1.7)])
c1.export_to_json("customer.json")

print(f"\nFailo skaitymas:")
c1 = Customer.from_json("customer.json")
print(c1.full_info)
print(c1.get_items())
