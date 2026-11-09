import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor


# Definizione della funzione che pulisce la tabella sostituendo i dati mancanti
def prepara_dati(df):
    # Creiamo una lista con le sole colonne numeriche che ci interessano
    colonne_numeriche = ['times_borrowed', 'rating', 'ratings_count', 'price', 'page_count', 'year_published']
    
    # Iniziamo un ciclo che scorre ogni colonna presente nella nostra lista
    for col in colonne_numeriche:
        # Verifichiamo con un IF se la colonna esiste effettivamente nel nostro DataFrame
        if col in df.columns:
            # Riempiamo le celle vuote sostituendole con la mediana dei valori di quella colonna
            df[col] = df[col].fillna(df[col].median())
            
    # Restituiamo il DataFrame con i dati riempiti
    return df



# PUNTO 1: CLUSTERING DEI LIBRI
# Definizione della funzione per il clustering con 4 gruppi di default
def esegui_clustering(df, n_clusters=4):
    # Stampiamo un messaggio di intestazione a schermo
    print("\n1. CLUSTERING DEI LIBRI")
    # Puliamo la tabella in ingresso richiamando la funzione scritta sopra
    df_ml = prepara_dati(df)
    
    # Scegliamo le 4 caratteristiche numeriche da far analizzare all'algoritmo
    features = ['times_borrowed', 'rating', 'price', 'page_count']
    # Selezioniamo solo queste colonne dalla nostra tabella e le salviamo in X
    X = df_ml[features]
    
    # Inizializziamo lo scalatore dei dati per mettere tutte le variabili sulla stessa scala
    scaler = StandardScaler()
    # Adattiamo e trasformiamo i numeri della matrice X (media 0 e varianza 1)
    X_scaled = scaler.fit_transform(X)
    
    # Inizializziamo l'algoritmo K-Means per creare 4 gruppi (random_state fissa i risultati)
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    # Troviamo i centri dei gruppi e salviamo il numero di cluster assegnato in una nuova colonna
    df_ml['Cluster'] = kmeans.fit_predict(X_scaled)
    
    # Calcoliamo la media di ogni caratteristica divisa per cluster, arrotondando a 2 decimali
    medie_cluster = df_ml.groupby('Cluster')[features].mean().round(2)
    # Stampiamo un'intestazione per la tabella di sintesi dei cluster
    print("\nCaratteristiche medie di ogni Cluster:")
    # Stampiamo a schermo la tabella delle medie per capire il profilo dei 4 gruppi
    print(medie_cluster)
    
    # Impostiamo la dimensione della finestra del grafico a 8 per 5 pollici
    plt.figure(figsize=(8, 5))
    # Creiamo uno scatter plot: Prezzo su X, Prestiti su Y e coloriamo i punti in base al Cluster
    plt.scatter(df_ml['price'], df_ml['times_borrowed'], c=df_ml['Cluster'], cmap='viridis', alpha=0.7)
    # Aggiungiamo il titolo principale del grafico
    plt.title("Segmentazione Libri: Prezzo vs Prestiti Totali")
    # Aggiungiamo l'etichetta all'asse delle X
    plt.xlabel("Prezzo (€)")
    # Aggiungiamo l'etichetta all'asse delle Y
    plt.ylabel("Numero Prestiti")
    # Aggiungiamo la legenda laterale con i colori corrispondenti ai Cluster ID
    plt.colorbar(label="Cluster ID")
    # Disegniamo la griglia di sfondo tratteggiata per rendere più leggibile il grafico
    plt.grid(True, linestyle='--', alpha=0.5)
    # Mostriamo a schermo la finestra con il grafico
    plt.show()
    
    # Restituiamo il DataFrame aggiornato col Cluster, l'oggetto kmeans e lo scaler
    return df_ml, kmeans, scaler



# PUNTO 2: PREDIZIONE PRESTITI (REGRESSIONE)

# Definizione della funzione per addestrare e confrontare i due modelli di regressione
def addestra_modello_predizione(df):
    # Stampiamo un messaggio di testo per l'avvio del modulo supervisionato
    print("\n2. PREDIZIONE PRESTITI (SUPERVISIONATO) ---")
    # Preparazione e pulizia condizionale dei dati della tabella
    df_ml = prepara_dati(df)
    
    # Definiamo quali colonne usare come variabili di input (caratteristiche del libro)
    features = ['year_published', 'price', 'page_count', 'rating', 'ratings_count']
    # Salviamo in X la matrice delle variabili indipendenti
    X = df_ml[features]
    # Salviamo in y la colonna del valore che vogliamo imparare a prevedere (prestiti totali)
    y = df_ml['times_borrowed']
    
    # Dividiamo i dati in 80% per l'addestramento (Train) e 20% per la verifica finale (Test)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
#MODELLO 1: REGRESSIONE LINEARE
    # Inizializziamo il modello di Regressione Lineare
    modello_lr = LinearRegression()
    # Addestriamo la Regressione Lineare sui dati di Train
    modello_lr.fit(X_train, y_train)
    # Facciamo le predizioni sui dati di Test
    y_pred_lr = modello_lr.predict(X_test)
    
#MODELLO 2:
    # Inizializziamo l'Albero di Decisione
    modello_dt = DecisionTreeRegressor(random_state=42)
    # Addestriamo l'Albero di Decisione sui dati di Train
    modello_dt.fit(X_train, y_train)
    # Facciamo le predizioni sui dati di Test
    y_pred_dt = modello_dt.predict(X_test)
    
    # CALCOLO SEMPLICE DELL'ERRORE
    # Convertiamo i valori reali di y_test in una lista semplice
    valori_reali = list(y_test)
    
    # Inizializziamo i sommatori degli errori a 0
    somma_errori_lr = 0
    somma_errori_dt = 0
    
    # Scorriamo con un ciclo FOR gli elementi per calcolare lo scarto tra reale e predetto
    for i in range(len(valori_reali)):
        # Differenza per la Regressione Lineare
        diff_lr = valori_reali[i] - y_pred_lr[i]
        # Se la differenza è negativa, la invertiamo con un semplice IF
        if diff_lr < 0:
            diff_lr = -diff_lr
        somma_errori_lr = somma_errori_lr + diff_lr
        
        # Differenza per l'Albero di Decisione
        diff_dt = valori_reali[i] - y_pred_dt[i]
        # Se la differenza è negativa, la invertiamo con un IF
        if diff_dt < 0:
            diff_dt = -diff_dt
        somma_errori_dt = somma_errori_dt + diff_dt
        
    # Calcoliamo l'errore medio dividendo la somma degli errori per il numero totale di elementi
    errore_medio_lr = somma_errori_lr / len(valori_reali)
    errore_medio_dt = somma_errori_dt / len(valori_reali)
    
    # Stampiamo a schermo il confronto fra l'errore medio dei due modelli
    print("\nConfronto Errore Medio dei Modelli di Regressione:")
    # Stampiamo l'errore della Regressione Lineare (arrotondato a 2 cifre decimali)
    print(f"1) Regressione Lineare-> Errore Medio: {round(errore_medio_lr, 2)} prestiti")
    # Stampiamo l'errore del Decision Tree
    print(f"2) Decision Tree -> Errore Medio: {round(errore_medio_dt, 2)} prestiti")
    
    # Restituiamo la LinearRegression da usare nel Menu
    return modello_lr


# Funzione che riceve dal menu i parametri numerici di un nuovo libro
def prevedi_nuovo_libro(modello, anno, prezzo, pagine, rating, num_voti):
    # Convertiamo i 5 valori ricevuti in un array bidimensionale NumPy richiesto dal modello
    nuovo_dato = np.array([[anno, prezzo, pagine, rating, num_voti]])
    # Chiediamo al modello di stimare i prestiti per questo nuovo libro inserito
    predizione = modello.predict(nuovo_dato)[0]
    # Restituiamo il valore numerico stimato arrotondato a 1 cifra decimale
    return round(predizione, 1)
    
   
#CODICE DI ESECUZIONE

# 1. Carichiamo il dataset dal file CSV
df_libri = pd.read_csv("books.csv")
print(f"Dataset caricato con successo! {len(df_libri)} libri trovati.")

# 2. Avviamo la funzione per il Clustering (Punto 1)
df_risultato, modello_kmeans, scaler = esegui_clustering(df_libri, n_clusters=4)

# 3. Avviamo la funzione per la Predizione Prestiti (Punto 2)
modello_predittivo = addestra_modello_predizione(df_libri)

# 4. Facciamo una prova di predizione su un nuovo libro
stima = prevedi_nuovo_libro(modello_predittivo, anno=2021, prezzo=18.5, pagine=350, rating=4.2, num_voti=120)
print(f"\nStima prestiti per il nuovo libro: {stima}")