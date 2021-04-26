from shop.item import Item


# Testavimas
i1 = Item("Morkos")
i2 = Item("Pienas", 2, 1.5)
i3 = Item("Batonas", price=0.5)

print(i1.full_info())
print(i2.full_info())
print(i3.full_info())

print(i1.to_dict())
print(i2.to_dict())
print(i3.to_dict())
