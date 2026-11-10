# Importazione
import Biblioteca_OOP as go
import mlbiblioteca as ml
import analisi as ad


def menu_oggetti():
    """Sottomenu dedicato alla Gestione ad Oggetti."""
    mentre_in_oggetti = True
    while mentre_in_oggetti:
        print("\n--- MENU: CREAZIONE AD OGGETTI ---")
        print("1. Visualizza dettagli di un libro")
        print("2. Aggiungi/Modifica stato del libro")
        print("3. Esegui metodo personalizzato dell'Oggetto")
        print("0. Torna al Menu Principale")
        
        scelta = input("\nSeleziona un'opzione: ").strip()
        
        if scelta == '1':
            print("\n[Esecuzione...] Mostra Dettagli Oggetto")
            go.mostra_dettagli_libro()
        elif scelta == '2':
            print("\n[Esecuzione...] Modifica Stato Libro")
            go.modifica_stato_libro()
        elif scelta == '3':
            print("\n[Esecuzione...] Metodo personalizzato")
            go.esegui_metodo()
        elif scelta == '0':
            mentre_in_oggetti = False
        else:
            print("Opzione non valida. Riprova.")


def menu_analisi_dati():
    """Sottomenu dedicato all'Analisi dei Dati."""
    mentre_in_analisi = True
    while mentre_in_analisi:
        print("\n--- MENU: ANALISI DEI DATI ---")
        print("1. Esplorazione iniziale (shape, info, describe, head)")
        print("2. Pulizia del dataset (rimozione duplicati e valori nulli)")
        print("3. Grafico a torta: Top 10 generi più presi in prestito")
        print("4. Grafico a barre: Top 10 libri più prestati")
        print("0. Torna al Menu Principale")
        
        scelta = input("\nSeleziona un'opzione: ").strip()
        
        if scelta == '1':
            print("\n[Esecuzione...] Esplorazione DataFrame")
            ad.esplora_dataframe()
        elif scelta == '2':
            print("\n[Esecuzione...] Pulizia Dataset")
            ad.pulisci_dataset()
        elif scelta == '3':
            print("\n[Esecuzione...] Grafico a Torta Generi")
            ad.mostra_grafico_torta()
        elif scelta == '4':
            print("\n[Esecuzione...] Grafico a Barre Top 10 Libri")
            ad.mostra_grafico_barre()
        elif scelta == '0':
            mentre_in_analisi = False
        else:
            print("Opzione non valida. Riprova.")


def menu_machine_learning():
    """Sottomenu dedicato ai Modelli di Machine Learning."""
    mentre_in_ml = True
    while mentre_in_ml:
        print("\n--- MENU: MACHINE LEARNING ---")
        print("1. Pre-elaborazione Dati")
        print("2. Addestramento Modello")
        print("3. Valutazione e Metriche")
        print("4. Effettua una nuova Previsione")
        print("0. Torna al Menu Principale")
        
        scelta = input("\nSeleziona un'opzione: ").strip()
        
        if scelta == '1':
            print("\n[Esecuzione...] Pre-processing Dati")
            ml.prepara_dati()
        elif scelta == '2':
            print("\n[Esecuzione...] Addestramento Modello")
            ml.addestra_modello()
        elif scelta == '3':
            print("\n[Esecuzione...] Valutazione Modello")
            ml.valuta_modello()
        elif scelta == '4':
            print("\n[Esecuzione...] Previsione")
            ml.predici()
        elif scelta == '0':
            mentre_in_ml = False
        else:
            print("Opzione non valida. Riprova.")


def menu_principale():
    """Menu principale che collega tutte le sezioni."""
    attivo = True
    while attivo:
        print("\n========================================")
        print("    SISTEMA DI GESTIONE & ANALISI LIBRI   ")
        print("========================================")
        print("1. Modulo 1: Creazione ad Oggetti")
        print("2. Modulo 2: Analisi Dati & Visualizzazione")
        print("3. Modulo 3: Machine Learning")
        print("0. Uscita")
        print("========================================")
        
        scelta = input("Inserisci la tua scelta (0-3): ").strip()
        
        if scelta == '1':
            menu_oggetti()
        elif scelta == '2':
            menu_analisi_dati()
        elif scelta == '3':
            menu_machine_learning()
        elif scelta == '0':
            print("\nGrazie per aver utilizzato il programma. Arrivederci!")
            attivo = False
        else:
            print("Scelta non valida. Inserisci un numero tra 0 e 3.")


# Avvio del menu
menu_principale() 