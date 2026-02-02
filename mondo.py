import random

class Stanza:
    def __init__(self, nome, descrizione, item, direzione):
        self.nome = nome
        self.descrizione = descrizione
        self.item = item
        self.direzione = direzione

    def __str__(self):
        return f"\n{self.nome}, {self.descrizione}, {self.item}, {self.direzione}\n"

class Stanze():
    def __init__(self):
        self.lista_stanze = []

    
    def aggiungi_stanze(self, lista_stanze):
        self.lista_stanze = lista_stanze

    def __str__(self):
        s = ''
        for i in self.lista_stanze:
            s += str(i)
        return s

room = Stanza(
    "room",
    "Melancholy and decadent. A vast circular hall with a soaring ceiling where dozens of tattered velvet banners hang like giant cobwebs. In the center, a dry fountain depicts a weeping angel; the floor is covered in a layer of dust so thin that every step kicks up small grey clouds. The silence is broken only by the faint whistle of wind filtering through the cracks in the walls.",
    "Health Potion (5 HP)",
    "nord"
)

room2 = Stanza(
    "room2",
    'Organic and unsettling. A natural corridor where the stone walls have been literally "embraced" by massive dark roots that seem to pulse with a faint, violet light. The air is thick, smelling of damp earth and ozone. On the ground, small bioluminescent mushrooms trace a path that seems to guide—or mislead—the traveler.',
    "Iron Sword (5 HP)",
    "ovest"
)

room3 = Stanza(
    "room3",
    "Hot and oppressive. The heat here is almost solid. Great iron crucibles hang from the ceiling by rusted chains, still filled with molten metal that casts long, distorted shadows. Cracked anvils and shattered weapons lie scattered everywhere, witnesses to a hasty flight or a sudden fit of rage.",
    "Damage Potion (+5 HP/hit)",
    "est"
)

room4 = Stanza(
    "room4",
    "Fragile and alien. A subterranean greenhouse where the glass panes, once clear, are now stained by an emerald mold that glows in the dark. Giant carnivorous plants sway slowly despite the lack of wind, and the sound of glass crunching underfoot rings out like an alarm bell to anyone listening.",
    "Health Potion (5 HP)",
    "sud"
)

room5 = Stanza(
    "room5",
    "Macabre and solemn. The walls are not made of stone, but of skulls and bones perfectly interlocked to form hypnotic geometric patterns. At the center of the room, a single throne of bone faces away from the entrance. There is no dust here; everything is clean, polished, and terrifyingly orderly.",
    "Iron Sword (5 HP)",
    "nord"
)

room6 = Stanza(
    "room6",
    "Mysterious and subaquatic. The water is ankle-deep, clear and freezing. Stone shelves reaching to the ceiling house tomes protected by magical bubbles, while soaked books float lazily like dead fish. Light reflects off the walls in bluish ripples, creating the illusion that the entire room is breathing underwater.",
    "Damage Potion (+5 HP/hit)",
    "nord"
)

room7 = Stanza(
    "room7",
    "Chaotic and chemical. Massive wooden tables are cluttered with bubbling alembics, singed parchments, and organs preserved in glass jars. A greenish vapor stagnates near the ceiling, and the pungent smell of sulfur and cinnamon attacks the nostrils. A chalkboard displays frantic calculations interrupted by a large blot of black ink.",
    "Health Potion (5 HP)",
    "est"
)

room8 = Stanza(
    "room8",
    "Claustrophobic and desperate. A tiny room where light filters in only from a grate in the ceiling, far too high to be reached. The walls are covered in notches carved into the rock and desperate graffiti. In a corner, a rotted straw mattress and a chipped wooden bowl are the only remnants of a life spent in isolation.",
    "Iron Sword (5 HP)",
    "ovest"
)

room9 = Stanza(
    "room9",
    "Spectral and opulent. A table dozens of meters long is set with finely crafted silverware and food that looks fresh, yet turns to dust at the slightest touch. Floating candles burn with bluish flames, illuminating empty chairs arranged as if an entire court were sitting down to dine in deathly silence.",
    "Damage Potion (+5 HP/hit)",
    "sud"
)

room10 = Stanza(
    "room10",
    "Steampunk and rhythmic. The floor is composed of enormous cogwheels that turn with an incessant metallic ticking. Jets of scalding steam burst at regular intervals from pipes running along the walls. It is a room in constant motion, where one false step could lead into the teeth of a hydraulic press.",
    "Health Potion (5 HP)",
    "nord"
)

mappa = Stanze()
mappa.aggiungi_stanze([room, room2, room3, room4, room5, room6, room7, room8, room9, room10])
print(mappa)