import random

def combattimento(giocatore, mostro):
    """
    Gestisce un ciclo di combattimento tra giocatore e mostro.
    Restituisce True se il giocatore vince, False se perde o fugge.
    """
    print(f"\n--- INIZIO COMBATTIMENTO ---")
    print(f"{giocatore.nome} (HP: {giocatore.hp}) vs {mostro.nome} (HP: {mostro.hp})")
    
    while giocatore.e_vivo() and mostro.e_vivo():
        # Turno del Giocatore
        print(f"\nTuo turno. HP: {giocatore.hp}/{giocatore.max_hp}")
        azione = input("Azione (a: attacca, u: usa, f: fuggi): ").strip().lower()
        
        if azione == 'a':
            danno = giocatore.attacco
            # Possibile variabilità del danno
            danno_effettivo = max(1, int(danno * random.uniform(0.8, 1.2)))
            mostro.subisci_danno(danno_effettivo)
            print(f"Colpisci {mostro.nome} per {danno_effettivo} danni!")
        elif azione == 'u':
            # Gestione Inventario in combattimento
            if not giocatore.inventario:
                print("Non hai oggetti!")
                continue # Non passa il turno
            
            print("\n=== INVENTARIO ===")
            for idx, oggett in enumerate(giocatore.inventario):
                print(f"{idx+1}. {oggett.nome} - {oggett.descrizione}")
            
            scelta_ogg = input("Usa oggetto (numero o invio per annullare): ")
            if scelta_ogg.isdigit():
                idx = int(scelta_ogg) - 1
                if 0 <= idx < len(giocatore.inventario):
                    ogg = giocatore.inventario[idx]
                    # Se è un'arma, magari non consuma il turno o lo consuma. 
                    # Per ora assumiamo che usare qualsiasi cosa consumi il turno.
                    res = ogg.usa(giocatore)
                    if res:
                         # Rimuovi se consumabile (dovremmo avere un flag consumabile, ma per ora controlliamo il tipo o il nome)
                         # Nel codice item.py, Pozione.usa ritorna True, Arma.usa ritorna True.
                         # Solo le pozioni dovrebbero sparire.
                         if "Potion" in ogg.nome or "Pozione" in ogg.nome:
                            giocatore.inventario.pop(idx)
                    else:
                        print("Non ha avuto effetto.")
                        continue # Non consuma il turno se fallisce (es. vita piena)
                else:
                    print("Oggetto inesistente.")
                    continue
            else:
                continue 
        elif azione == 'f':
            if random.random() > 0.4: # 60% chance di fuga
                print("Sei riuscito a fuggire!")
                return False
            else:
                print("Non riesci a svignartela!")
        else:
            print("Non capisco questo comando. Perdi il turno per esitazione!")

        if not mostro.e_vivo():
            print(f"HAI SCONFITTO {mostro.nome}!")
            return True

        # Turno del Mostro
        print(f"\nTurno di {mostro.nome}...")
        danno_mostro = max(1, int(mostro.attacco * random.uniform(0.8, 1.2)))
        giocatore.subisci_danno(danno_mostro)
        print(f"{mostro.nome} ti colpisce per {danno_mostro} danni!")
    
    if not giocatore.e_vivo():
        print(f"\n{giocatore.nome} è stato sconfitto...")
        return False
        
    return True
