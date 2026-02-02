class Item:
    def __init__(self, name: str):
        self.name = name

class Arm(Item):
    def __init__(self, name: str, damage: int):
        self.name = name
        self.damage = damage

class Potion(Item):
    def __init__(self, name: str, healing_amount: int):
        self.name = name
        self.healing_amount = healing_amount

Spada = Arm("Spada", 4)
coltello = Arm("Coltello", 2)

pozione_piccola = Potion("Pozione Piccola", 2)
pozione_grande = Potion("Pozione Grande", 4)
