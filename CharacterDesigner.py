# creazioni delle classi giocatori e nemici 

# definizione classe 

class Character:
    def __init__ (self,name:str,health:int,attack:int):
        self.name : str = name
        self.health : int = health
        self.attack : int = attack
    
    def alive(self):
        return self.health>0
    
    def wasted(self):
        return self.health<=0
    
    def takedamage(self,damage):
        self.health -= damage
        print(f"{self.name} lose {damage} HP remaining {self.health} ")
    
    def attack(self,target: "Character"):
        print(f"{self.name} attack {target.name}")
        target.takedamage(self.attack)

#es aim

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


# creazione estensione della classe per l'eroe

class Hero(Character):
    def __init__ (self,name:str,health:int,attack:int):
        #super init serve a richiama il costruttore della classe base 
        super().__init__(name,health,attack)
        self.arm = None 
        self.inventory = [] 

    # funzione per equipaggare arma 

    def equi_arma(self,arm:Arm): 
       self.arm = arm 
       print(f"{self.name} equips {arm.name} (+{arm.damage} attack)") 
    
    # funzione per aggiungere oggetti all'inventario 

    def add_item(self,item:Item):
        self.inventory.append(item)
        print(f"add {item.name}")
    
    # funzione per curarsi con la pozione

    def use_potion(self,potion:Potion):
        if potion in self.inventory:
            self.health += potion.healing_amount
            self.inventory.remove(potion)
            print(f"{self.name} used {potion.name} and heals {potion.healing_amount} HP")

        else:
            print("no {potion.name} not in the inventory")
    
    # funzione attacco con un arma 

    def attack_target(self, target: Character):
        total_attack = self.attack
        if self.arm:  # se ha un'arma
            total_attack += self.arm.damage
            print(f"{self.name} attacks {target.name} with {self.arm.name} for {total_attack} damage")
        else: 
            print(f"{self.name} attacks {target.name} with hands for {total_attack} damage")
    
        target.takedamage(total_attack)


# creazione personaggi 


hero_player = Hero("Hero", 100, 1)        
monster = Character("Giant Skeleton", 100, 3)  






