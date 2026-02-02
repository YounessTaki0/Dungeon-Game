import sys
import random
# Aggiungiamo la root path al path di sistema se necessario, ma di solito l'esecuzione da main.py funziona.
from models import mondo
from models.character import Giocatore, Mostro
from models.item import Pozione, Arma
from engine.combat import combattimento

class Gioco:
    def __init__(self):
        self.giocatore = None
        # Utilizziamo la mappa esposta da mondo.py
        self.mappa = mondo.mappa
        self.posizione_idx = 0 
        self.game_over = False

    def setup(self):
        print("Benvenuto in Dungeon Game!")
        try:
            with open("README.md", "r", encoding="utf-8") as f:
                print("\n" + f.read() + "\n")
        except FileNotFoundError:
            print("Storia non disponibile.")
            
        nome = input("Inserisci il nome del tuo eroe: ")
        self.giocatore = Giocatore(nome)
        print(f"Ciao {self.giocatore.nome}! Inizia la tua avventura...")
        input("Premi Invio per continuare...")

    def parse_item(self, item_description):
        """Traduce la stringa dell'item di mondo.py in un oggetto di gioco."""
        if not item_description or item_description == "Nessuno":
            return None
        
        if "Potion" in item_description:
            # Esempio: "Health Potion (5 HP)" -> Pozione cura 5
            # Parsing molto semplice
            return Pozione("Pozione Salute", 5)
        elif "Sword" in item_description:
            return Arma("Spada di Ferro", 5)
        
        # Default se non riconosciamo
        return None

    def gioca(self):
        self.setup()

        while not self.game_over and self.giocatore.e_vivo():
            # Ottieni la stanza corrente
            stanza = self.mappa.lista_stanze[self.posizione_idx]
            
            print("\n" + "="*40)
            print(f"LUOGO: {stanza.nome}")
            print("-" * 40)
            print(stanza.descrizione)
            
            # Evento Mostro Casuale
            if random.random() < 0.4: # 40% probabilità incontro
                input("\nQualcosa si muove nell'ombra... (Premi Invio)")
                mostro = Mostro("Guardiano Oscuro", hp=random.randint(20, 40), attacco=random.randint(4, 8))
                vittoria = combattimento(self.giocatore, mostro)
                
                if not vittoria and not self.giocatore.e_vivo():
                    self.game_over = True
                    break
                elif not vittoria:
                    # Fuga
                    pass
            
            if self.game_over: break

            # Interazione
            print(f"\nHP: {self.giocatore.hp}/{self.giocatore.max_hp}")
            
            # Oggetti nella stanza?
            oggetto_stanza = self.parse_item(stanza.item)
            if oggetto_stanza:
                print(f"Vedi un oggetto interessante: {stanza.item}")

            print("\nComandi: [n]ord, [s]ud, [e]st, [o]vest, [p]rendi, [i]nventario, [a]ttacca, [q]uit")
            scelta = input("Cosa fai? ").lower().strip()

            if scelta in ['n', 's', 'e', 'o']:
                direzione_stanza = stanza.direzione.lower() # es. "nord"
                
                # Logica di movimento semplificata:
                # Se la direzione scelta corrisponde alla 'direzione' della stanza in mondo.py, 
                # assumiamo che porti alla stanza successiva nella lista.
                # Nota: mondo.py non è un grafo completo, è una lista. Adattiamo la logica.
                
                scelta_estesa = {'n': 'nord', 's': 'sud', 'e': 'est', 'o': 'ovest'}[scelta]
                
                if scelta_estesa == direzione_stanza:
                    print(f"Ti incammini verso {scelta_estesa}...")
                    if self.posizione_idx < len(self.mappa.lista_stanze) - 1:
                        self.posizione_idx += 1
                    else:
                        print("Hai trovato l'uscita del dungeon! VITTORIA!")
                        self.game_over = True
                else:
                    print("Da quella parte c'è solo un muro o un vicolo cieco.")
            
            elif scelta == 'p':
                if oggetto_stanza:
                    self.giocatore.aggiungi_oggetto(oggetto_stanza)
                    print(f"Hai preso: {oggetto_stanza.nome}")
                    # Rimuoviamo l'oggetto dalla stanza (mappa è in memoria)
                    stanza.item = "Nessuno"
                else:
                    print("Non c'è nulla da prendere qui.")
            
            elif scelta == 'a':
                print("Non c'è nessun nemico qui al momento. Tieni la spada pronta!")

            elif scelta == 'i':
                print("\n=== INVENTARIO ===")
                if not self.giocatore.inventario:
                    print("Vuoto.")
                else:
                    for idx, oggett in enumerate(self.giocatore.inventario):
                        print(f"{idx+1}. {oggett.nome} - {oggett.descrizione}")
                
                    usa = input("Vuoi usare un oggetto? (numero o 'no'): ")
                    if usa.isdigit():
                        idx = int(usa) - 1
                        if 0 <= idx < len(self.giocatore.inventario):
                            ogg = self.giocatore.inventario[idx]
                            consumato = ogg.usa(self.giocatore)
                            if consumato and isinstance(ogg, Pozione):
                                self.giocatore.inventario.pop(idx)

            elif scelta == 'q':
                print("Abbandoni l'avventura.")
                self.game_over = True
            
            else:
                print("Comando non valido.")

        print("Grazie per aver giocato!")
