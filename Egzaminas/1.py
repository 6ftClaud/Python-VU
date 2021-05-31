# Sukuriama funkcija kuri priima viena kintamaji
def order_and_square(sarasas):
    # try/except blokas tikrina ar sarase tik skaiciai
    try:
        # surusiuoja skaicius sarase
        sarasas.sort()
        # kiekvienas skaicius sarase pakeliamas kvadratu
        sarasas = [i * i for i in sarasas]
        # grazinamas sarasas
        return sarasas
    except TypeError:
        print("Sarase turi buti tik skaiciai")


print(order_and_square([2, 1, 10, 5]))
