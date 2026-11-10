# Importazione
import Biblioteca_OOP as go
import mlbiblioteca as ml
import analisi as ad



def menu_analisi_dati():
    """Sottomenu dedicato all'Analisi dei Dati."""
    mentre_in_analisi = True
    while mentre_in_analisi:
        print("\n--- MENU: ANALISI DEI DATI---")
        print("1. Esplorazione iniziale (shape, info, describe, head)")
        print("2. Pulizia del dataset (uniformazione sezioni, duplicati, nulli)")
        print("3. Grafico a Torta: Top 10 generi più presi in prestito")
        print("4. Grafico a Barre: Top 10 libri più prestati")
        print("5. Grafico a Barre: Prestiti per mese dell'ultimo prestito")
        print("6. Scatter Plot Interattivo: Valutazione vs Prestiti (Plotly)")
        print("7. Grafico a Barre: Media prestiti per sezione (Plotly)")
        print("0. Torna al Menu Principale")
        
        scelta = input("\nSeleziona un'opzione: ").strip()
        
        if scelta == '1':
            ad.esplora_dataframe()
        elif scelta == '2':
            ad.pulisci_dataset()
        elif scelta == '3':
            ad.mostra_grafico_torta()
        elif scelta == '4':
            ad.mostra_grafico_barre_top10()
        elif scelta == '5':
            ad.mostra_grafico_mesi()
        elif scelta == '6':
            ad.mostra_scatter_plotly()
        elif scelta == '7':
            ad.mostra_prestiti_medi_plotly()
        elif scelta == '0':
            mentre_in_analisi = False
        else:
            print("Opzione non valida. Riprova.")


def menu_machine_learning():
    """Sottomenu dedicato ai Modelli di Machine Learning."""
    mentre_in_ml = True
    while mentre_in_ml:
        print("\n--- MENU: MACHINE LEARNING ---")
        print("1. Segmentazione Libri (Clustering K-Means & PCA 2D)")
        print("2. Valutazione e Confronto Modelli (Linear Regression vs Decision Tree)")
        print("3. Previsione Prestiti per un Nuovo Libro")
        print("4. Sistema di Raccomandazione Libri (Cosine Similarity)")
        print("0. Torna al Menu Principale")
        
        scelta = input("\nSeleziona un'opzione: ").strip()
        
        if scelta == '1':
            print("\n[Esecuzione...] Clustering K-Means e generazione grafico PCA...")
            ml.esegui_clustering(ad.df, n_clusters=4)
            
        elif scelta == '2':
            print("\n[Esecuzione...] Addestramento e confronto modelli di Regressione...")
            ml.addestra_modello_predizione(ad.df)
            
        elif scelta == '3':
            print("\n--- PREVISIONE PRESTITI PER UN NUOVO LIBRO ---")
            anno = float(input("Anno di pubblicazione (es. 2021): "))
            prezzo = float(input("Prezzo in € (es. 18.5): "))
            pagine = float(input("Numero di pagine (es. 350): "))
            rating = float(input("Rating (es. 4.2): "))
            voti = float(input("Numero di voti/recensioni (es. 120): "))
            
            # Addestra il modello al momento e calcola subito la stima
            modello = ml.addestra_modello_predizione(ad.df)
            stima = ml.prevedi_nuovo_libro(modello, anno, prezzo, pagine, rating, voti)
            print(f"\n-> Risultato: Il libro otterrà circa {stima} prestiti totali.")
                
        elif scelta == '4':
            titolo_cercato = input("\nInserisci il titolo (o parte di esso) del libro da cercare: ").strip()
            ml.raccomanda_libri(ad.df, titolo_cercato)
                
        elif scelta == '0':
            mentre_in_ml = False
        else:
            print("Opzione non valida. Scegli un numero da 0 a 4.")

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