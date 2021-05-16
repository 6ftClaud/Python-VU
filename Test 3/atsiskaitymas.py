# PIRMA UZDUOTIS
# Importuojami reikalingi moduliai
import sqlalchemy as sql
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship


# Deklaruojama baze modeliams
base = declarative_base()


# Sukuriamas "Shop" table paveldint "base"
class Shop(base):
    # Nurodomas sio table vardas duomenu bazeje
    __tablename__ = "shop"

    # Nurodomi sio table kintamieji
    id = sql.Column(sql.Integer, primary_key=True, autoincrement=True)
    name = sql.Column(sql.String(40), nullable=False)
    address = sql.Column(sql.String(100))
    items = relationship("Item")

    def __repr__(self):
        return f"<Shop({self.name}, {self.address}, {self.items})>"


# Sukuriamas "Item" table paveldint "base"
class Item(base):
    # Nurodomas sio table vardas duomenu bazeje
    __tablename__ = "item"

    # Nurodomi sio table kintamieji
    id = sql.Column(sql.Integer, primary_key=True, autoincrement=True)
    barcode = sql.Column(sql.String(32), unique=True)
    name = sql.Column(sql.String(40), nullable=False)
    description = sql.Column(sql.String(200), default='EMPTY')
    unit_price = sql.Column(sql.Numeric(10, 2), nullable=False, default="1.00")
    created_at = sql.Column(sql.DateTime)
    shop_id = sql.Column(sql.Integer(), sql.ForeignKey('shop.id'))
    shop = relationship("Shop")
    components = relationship("Component")

    def __repr__(self):
        return f"<Item({self.barcode}, {self.name}, {self.description}, {self.unit_price}, {self.created_at}, {self.shop_id}, {self.shop}, {self.components})>"


# Sukuriamas "Component" table paveldint "base"
class Component(base):
    # Nurodomas sio table vardas duomenu bazeje
    __tablename__ = "component"

    # Nurodomi sio table kintamieji
    id = sql.Column(sql.Integer, primary_key=True, autoincrement=True)
    name = sql.Column(sql.String(20))
    quantity = sql.Column(sql.Numeric(10, 2), default="1.00")
    item_id = sql.Column(sql.Integer(), sql.ForeignKey('item.id'))
    item = relationship("Item")

    def __repr__(self):
        return f"<Item({self.name}, {self.quantity}, {self.item_id}, {self.item})>"


"""
default - nurodo numatyta reiksme
autoincrement - su kiekvienu irasu didina reiksme vienetu
nullable - jei nullable reiksme lygi False, tai reiskia kad tas kintamasis privalo tureti reiksme
primary_key - nurodo kad tai pagrindine table reiksme
ForeignKey - nurdodo kad tai reiksme is kito table
"""

# ANTRA UZDUOTIS
engine = sql.create_engine("sqlite:///:memory:")
base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

iki = Shop(name="IKI", address="Kaunas, Iki gatvė 1")
maxima = Shop(name="MAXIMA", address="Kaunas, Maksima gatvė 2")

session.add_all([iki, maxima])
session.commit()

# Sukuriami IKI parduotuves prekes - Item klases objektai
iki.items = [
    Item(barcode="112233112233", name="Žemaičių duona", unit_price=1.55),
    Item(barcode='33333222111', description="Pienas iš Žemaitijos", name="Žemaičių pienas", unit_price=2.69)
]

maxima.items = [
    Item(barcode='99898989898', name='Aukštaičių duona', unit_price=1.65),
    Item(barcode='99919191991', description='Pienas iš Aukštaitijos', name='Aukštaičių pienas', unit_price=2.99)
]

# Sukuriami tu klases objektu komponentai
iki.items[0].components = [
    Component(name='Miltai', quantity=1.50),
    Component(name='Vanduo', quantity=1.00),
]

iki.items[1].components = [
    Component(name='Pienas', quantity=1.00)
]

maxima.items[0].components = [
    Component(name='Miltai', quantity=1.60),
    Component(name='Vanduo', quantity=1.10)
]

maxima.items[1].components = [
    Component(name='Pienas', quantity=1.10)
]

session.add_all([iki.items[0], iki.items[1], maxima.items[0], maxima.items[1]])
session.commit()

# TRECIA UZDUOTIS
