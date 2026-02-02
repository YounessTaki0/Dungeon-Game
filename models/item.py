class Oggetto:
    """Classe base per gli oggetti del gioco."""
    def __init__(self, nome, descrizione):
        self.nome = nome
        self.descrizione = descrizione

    def usa(self, personaggio):
        raise NotImplementedError("Devi implementare il metodo usa")

class Pozione(Oggetto):
    """Classe per le pozioni curative."""
    def __init__(self, nome, cura):
        super().__init__(nome, f"Cura {cura} HP")
        self.cura = cura

    def usa(self, personaggio):
        diff = personaggio.max_hp - personaggio.hp
        if diff > 0:
            recupero = min(diff, self.cura)
            personaggio.hp += recupero
            print(f"{personaggio.nome} usa {self.nome} e recupera {recupero} HP!")
            return True
        else:
            print(f"{personaggio.nome} ha già il massimo degli HP.")
            return False

    @classmethod
    def pozione_piccola(cls):
        return cls("Pozione Piccola", 2)

    @classmethod
    def pozione_grande(cls):
        return cls("Pozione Grande", 4)

class Arma(Oggetto):
    """Classe per le armi."""
    def __init__(self, nome, danno_extra):
        super().__init__(nome, f"Aumenta attacco di {danno_extra}")
        self.danno_extra = danno_extra

    def usa(self, personaggio):
        # Questo metodo potrebbe equipaggiare l'arma.
        personaggio.attacco += self.danno_extra
        print(f"{personaggio.nome} equipaggia {self.nome}! Attacco base aumentato di {self.danno_extra}.")
        return True

    @classmethod
    def spada(cls):
        return cls("Spada", 4)

    @classmethod
    def coltello(cls):
        return cls("Coltello", 2)


