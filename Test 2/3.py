from shop.item import Food, Drink


# Testavimas
f1 = Food("Batonas", 2, 1.3)
f2 = Food("Sviestas", 1, 1.3)

d1 = Drink("CocaCola", 3, 1.7)
d2 = Drink("Sprite", 2, 1.7)

print(f1.full_info())
print(f2.full_info())
print(d1.full_info())
print(d2.full_info())
