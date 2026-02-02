class Personaggio:
    """Classe base per tutti i personaggi del gioco."""
    def __init__(self, nome, hp, attacco):
        self.nome = nome
        self.hp = hp
        self.max_hp = hp
        self.attacco = attacco

    def e_vivo(self):
        """Restituisce True se il personaggio ha HP > 0"""
        return self.hp > 0

    def subisci_danno(self, danno):
        """Riduce gli HP del personaggio in base al danno ricevuto."""
        self.hp -= danno
        if self.hp < 0:
            self.hp = 0

    def attacca(self, bersaglio):
        """Esegue un attacco contro un bersaglio."""
        pass # Implementazione specifica nelle sottoclassi o logica generica

class Giocatore(Personaggio):
    """Classe che rappresenta il giocatore umano."""
    def __init__(self, nome):
        super().__init__(nome, hp=100, attacco=10)
        self.inventario = []

    def aggiungi_oggetto(self, oggetto):
        self.inventario.append(oggetto)

class Mostro(Personaggio):
    """Classe che rappresenta un nemico."""
    def __init__(self, nome, hp, attacco):
        super().__init__(nome, hp, attacco)
