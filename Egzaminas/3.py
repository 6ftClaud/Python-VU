# Importuojamos reikalingos bibliotekos
from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey,
    create_engine,
    func,
)
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
import datetime

engine = create_engine("sqlite:///:memory:", echo=False)
Base = declarative_base()


# Kintamuju klasese manau nereikia komentuoti
# Aprasoma Channel klase
class Channel(Base):
    __tablename__ = "channels"
    id = Column(Integer, primary_key=True)
    name = Column(String(40), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now())
    shows = relationship("Show")


# aprašoma Show klase
class Show(Base):
    __tablename__ = "shows"
    id = Column(Integer, primary_key=True)
    chanel_id = Column(Integer, ForeignKey("channels.id"))
    start_datetime = Column(DateTime, default=datetime.datetime.now(), nullable=False)
    rate = Column(Integer)
    name = Column(String(40), nullable=False)
    channel = relationship("Channel")


# Sukuriama sesija
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Testuojama
# Sukuriami 2 kanalai
Netflix = Channel(name="Netflix")
HBO = Channel(name="HBO")

# Tie 2 kanalai irasomi i duomenu base su add_all ir commit
session.add_all([Netflix, HBO])
session.commit()

# Surasomos kanalu laidos
Netflix.shows = [
    Show(name="Mr. Robot", rate=8),
    Show(name="The Queen's Gambit", rate=10),
]

HBO.shows = [
    Show(name="The Sopranos", rate=8),
    Show(name="Game of Thrones", rate=10),
    Show(name="Band of Brothers", rate=9),
]

# Pakeitimai irasomi i duomenu baze
session.add_all(
    [Netflix.shows[0], Netflix.shows[1], HBO.shows[0], HBO.shows[1], HBO.shows[2]]
)
session.commit()

# Uzklausos
# atspausdintų kiekvieno kanalo laidų skaičių
print("Kiekvieno kanalo laidu skaicius")
# Sukuria uzklausa kuri grazina laidu skaiciu pagal sugrupuota kanala
for name, count in (
    session.query(Channel, func.count(Show.id)).join(Show).group_by(Channel).all()
):
    print(name.name, count)

# atspausdintų suminį kiekvieno kanalo laidų reitingą
print("Suminis visu laidu reitingas")
# Sukuria uzklausa kuri grazina susumuotus laidu reitingus pagal sugrupuota kanala
for name, rating in (
    session.query(Channel, func.sum(Show.rate)).join(Show).group_by(Channel).all()
):
    print(name.name, rating)

# atspausdintų kiekvieno kanalo laidą, kuri turi didžiausią reitingą
print("Laida kanale kuri turi didziausia reitinga")
for item in session.query(Channel):
    shows = []
    # Iteruoja per laidas kurios turi kanalo pavadinima
    for show in session.query(Show).filter(Show.channel.has(name=item.name)):
        # Prie shows kintamojo prideda (varda, reitinga)
        shows.append((show.name, show.rate))
    best_show = ("Show name", 0)
    # Iteruojama per tuple shows kintamaji
    for show in enumerate(shows):
        # Jei laidos reitingas aukstesnis nei dabartinis, pakeiciamas best_show
        if show[1][1] > best_show[1]:
            best_show = (show[1][0], show[1][1])
    print(item.name, best_show)
