import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics.pairwise import cosine_similarity


# FUNZIONE PER SISTEMARE E PULIRE I DATI MANCANTI NEL DATAFRAME
def prepara_dati(df):
    # Salviamo in una lista i nomi delle colonne numeriche su cui vogliamo lavorare
    colonne_numeriche = ['times_borrowed', 'rating', 'ratings_count', 'price', 'page_count', 'year_published']
    
    # Facciamo un ciclo for per controllare una per una le colonne numeriche
    for col in colonne_numeriche:
        # Se la colonna esiste davvero all'interno della nostra tabella
        if col in df.columns:
            # Sostituiamo i valori nulli o vuoti con il valore mediano di quella specifica colonna
            df[col] = df[col].fillna(df[col].median())
            
    # Restituiamo il DataFrame pulito con tutti i buchi riempiti
    return df


# PUNTO 1: CLUSTERING K-MEANS + RIDUZIONE 2D CON PCA
def esegui_clustering(df, n_clusters=4):
    # Stampiamo un'intestazione per capire che siamo dentro la funzione del Clustering
    print("\n--- 1. CLUSTERING DEI LIBRI (K-MEANS & PCA) ---")
    
    # Creiamo una copia del DataFrame originale e lo puliamo usando la funzione scritta sopra
    df_ml = prepara_dati(df.copy())
    
    # Scegliamo 4 caratteristiche numeriche per decidere come raggruppare i libri
    features = ['times_borrowed', 'rating', 'price', 'page_count']
    X = df_ml[features]
    
    # Inizializziamo lo StandardScaler
    scaler = StandardScaler()
    # Adattiamo lo scaler e trasformiamo i dati numerici della matrice X
    X_scaled = scaler.fit_transform(X)
    
    # Creiamo il modello K-Means impostando 4 gruppi (cluster), con random_state=42 per avere sempre gli stessi risultati
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)  #Ripeti l'intero processo di clustering per 10 volte partendo da punti iniziali diversi, e alla fine dammi solo il risultato migliore
    # Addestriamo K-Means sui dati trasformati e assegniamo a ciascun libro il suo numero di Cluster (da 0 a 3)
    df_ml['Cluster'] = kmeans.fit_predict(X_scaled)
    
    # Calcoliamo la media delle 4 caratteristiche per ogni gruppo e arrotondiamo a 2 decimali
    medie_cluster = df_ml.groupby('Cluster')[features].mean().round(2)
    print("\nCaratteristiche medie di ogni Cluster:")
    # Stampiamo la tabella riassuntiva a schermo per capire le caratteristiche dei 4 gruppi
    print(medie_cluster)
    
    # Salviamo l'intera tabella aggiornata col numero di Cluster in un nuovo file CSV per non perdere i dati
    df_ml.to_csv("libri_con_cluster.csv", index=False)
    print("\n-> Risultati del Clustering salvati nel file 'libri_con_cluster.csv'!")
    
    # Usiamo PCA per schiacciare le 4 colonne numeriche in 2 sole coordinate (PC1 e PC2) mantenendo le informazioni principali
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_scaled)
    
    # Prepariamo la figura del grafico con dimensioni 8x5 pollici
    plt.figure(figsize=(8, 5))
    # Disegniamo i punti in 2D: asse X = PC1, asse Y = PC2, colorando ciascun punto in base al suo Cluster
    scatter = plt.scatter(X_pca[:, 0], X_pca[:, 1], c=df_ml['Cluster'], cmap='viridis', alpha=0.7)
    # Titolo del grafico
    plt.title("Visualizzazione 2D dei Cluster tramite PCA")
    # Etichette degli assi
    plt.xlabel("Componente Principale 1 (PC1)")
    plt.ylabel("Componente Principale 2 (PC2)")
    # Aggiungiamo la barra dei colori laterale per distinguere i gruppi
    plt.colorbar(scatter, label="Cluster ID")
    # Disegniamo le linee della griglia sotto al grafico per leggerlo meglio
    plt.grid(True, linestyle='--', alpha=0.5)
    # Adattiamo i margini della figura automaticamente
    plt.tight_layout()
    
    # Salviamo l'immagine del grafico sul computer in formato PNG prima di mostrarla
    plt.savefig("grafico_cluster_pca.png")
    print("-> Grafico del clustering salvato come 'grafico_cluster_pca.png'")
    # Mostriamo la finestra del grafico a schermo
    plt.show()
    
    # Restituiamo il dataframe elaborato, il modello kmeans addestrato e lo scaler
    return df_ml, kmeans, scaler


# PUNTO 2: REGRESSIONE PER PREVEDERE IL NUMERO DI PRESTITI
def addestra_modello_predizione(df):
    # Messaggio di testo per indicare la seconda parte (apprendimento supervisionato)
    print("\n--- 2. PREDIZIONE PRESTITI (SUPERVISIONATO) ---")
    # Puliamo i dati prima di procedere
    df_ml = prepara_dati(df)
    
    # Scegliamo 5 colonne come fattori di input (variabili indipendenti X)
    features = ['year_published', 'price', 'page_count', 'rating', 'ratings_count']
    X = df_ml[features]
    # Definiamo l'obiettivo y: il valore numerico che vogliamo far indovinare al modello (prestiti totali)
    y = df_ml['times_borrowed']
    
    # Spezziamo i dati: 80% per addestrare i modelli (Train) e 20% per testarli su dati mai visti (Test)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # --MODELLO 1: REGRESSIONE LINEARE--
    # Creiamo il modello di Regressione Lineare (cerca una relazione rettilinea tra le variabili)
    modello_lr = LinearRegression()
    # Alleniamo il modello facendogli vedere le X_train e le y_train
    modello_lr.fit(X_train, y_train)
    # Chiediamo al modello di stimare le y usando solo le X del gruppo di test
    y_pred_lr = modello_lr.predict(X_test)
    
    # --MODELLO 2: ALBERO DI DECISIONE--
    # Creiamo un Albero di Decisione per la regressione
    modello_dt = DecisionTreeRegressor(random_state=42)
    # Alleniamo l'Albero di Decisione sui dati di allenamento
    modello_dt.fit(X_train, y_train)
    # Chiediamo all'Albero di fare le sue predizioni sul gruppo di test
    y_pred_dt = modello_dt.predict(X_test)
    
    #CALCOLO DELL'ERRORE MEDIO
    # Trasformiamo la colonna y_test in una lista semplice di numeri reali
    valori_reali = list(y_test)
    # Inizializziamo a zero i due contenitori della somma degli errori
    somma_errori_lr = 0
    somma_errori_dt = 0
    
    # Scorriamo uno per uno tutti i valori di test
    for i in range(len(valori_reali)):
        # Calcoliamo lo scarto tra il valore reale e quello stimato dalla Regressione Lineare
        diff_lr = valori_reali[i] - y_pred_lr[i]
        # Se il risultato della sottrazione viene negativo, lo trasformiamo in positivo (valore assoluto)
        if diff_lr < 0:
            diff_lr = -diff_lr
        # Sommiamo lo scarto al totale degli errori di Regressione Lineare
        somma_errori_lr += diff_lr
        
        # Calcoliamo lo scarto per l'Albero di Decisione
        diff_dt = valori_reali[i] - y_pred_dt[i]
        # Se lo scarto è negativo, lo invertiamo
        if diff_dt < 0:
            diff_dt = -diff_dt
        # Sommiamo lo scarto al totale degli errori dell'Albero
        somma_errori_dt += diff_dt
        
    # Calcoliamo l'errore medio dividendo la somma degli scarti per il totale dei libri verificati
    errore_medio_lr = somma_errori_lr / len(valori_reali)
    errore_medio_dt = somma_errori_dt / len(valori_reali)
    
    # Stampiamo il confronto a schermo
    print("\nConfronto Errore Medio dei Modelli di Regressione:")
    print(f"1) Regressione Lineare -> Errore Medio: {round(errore_medio_lr, 2)} prestiti")
    print(f"2) Decision Tree       -> Errore Medio: {round(errore_medio_dt, 2)} prestiti")
    
    # Restituiamo il modello di Regressione Lineare per usarlo più avanti nelle predizioni singole
    return modello_lr


# Funzione per inserire i dati di un solo libro manuale ed estrarre la stima dei prestiti
def prevedi_nuovo_libro(modello, anno, prezzo, pagine, rating, num_voti):
    # Convertiamo le 5 informazioni inserite in una matrice bidimensionale 1x5 richiesta da scikit-learn
    nuovo_dato = np.array([[anno, prezzo, pagine, rating, num_voti]])
    # Usiamo il modello già addestrato per calcolare la stima
    predizione = modello.predict(nuovo_dato)[0]
    # Restituiamo la stima arrotondata a una cifra decimale
    return round(predizione, 1)

# PUNTO 3: SISTEMA DI RACCOMANDAZIONE
def raccomanda_libri(df, titolo_ricerca):
    print(f"\n--- 3. SISTEMA DI RACCOMANDAZIONE LIBRI ---")
    # Puliamo una copia del DataFrame
    df_ml = prepara_dati(df.copy())
    
    # Cerchiamo dentro la colonna 'title' se c'è una corrispondenza ignorando le maiuscole/minuscole
    maschera = df_ml['title'].astype(str).str.lower().str.contains(titolo_ricerca.lower())
    libri_trovati = df_ml[maschera]
    
    # Se il filtro non trova nessuna corrispondenza...
    if libri_trovati.empty:
        print(f"Nessun libro trovato con la parola '{titolo_ricerca}'.")
    else:
        # Prendiamo l'indice del primo libro trovato tra quelli corrispondenti
        idx_libro = libri_trovati.index[0]
        # Recuperiamo la stringa del titolo esatto
        titolo_esatto = df_ml.loc[idx_libro, 'title']
        print(f"Libro selezionato: '{titolo_esatto}'")
        
        # Scegliamo 4 colonne numeriche per calcolare quanto i libri si somigliano
        features = ['times_borrowed', 'rating', 'price', 'page_count']
        scaler = StandardScaler()
        # Scaliamo la matrice dei dati
        X_scaled = scaler.fit_transform(df_ml[features])
        
        # Calcoliamo la matrice di similarità Coseno tra tutte le coppie di libri
        sim_matrix = cosine_similarity(X_scaled)
        # Estraiamo tutta la riga dei punteggi di similarità relativa al nostro libro selezionato
        punteggi_simili = list(enumerate(sim_matrix[idx_libro]))
        
        # Ordiniamo i libri dal più simile al meno simile, escludendo la posizione [0] che è il libro stesso
        punteggi_ordinati = sorted(punteggi_simili, key=lambda x: x[1], reverse=True)[1:4]
        
        print("\nEcco i 3 libri consigliati per caratteristiche simili:")
        # Ciclo per stampare a schermo i 3 titoli più vicini matematicamente
        for idx, score in punteggi_ordinati:
            titolo_rec = df_ml.loc[idx, 'title']
            # Se esiste la colonna autore la usiamo, altrimenti mettiamo una scritta standard
            autore_rec = df_ml.loc[idx, 'author'] if 'author' in df_ml.columns else "Autore Sconosciuto"
            # Stampiamo titolo, autore e percentuale di affinità
            print(f"- '{titolo_rec}' di {autore_rec} (Affinità: {round(score * 100, 1)}%)")


# BLOCCO DI TEST / ESECUZIONE DI PROVA
# Leggiamo il dataset CSV iniziale tramite pandas
df_libri = pd.read_csv("books.csv")
print(f"Dataset caricato con successo! {len(df_libri)} libri trovati.")

# 1. Avviamo la funzione di Clustering K-Means e visualizzazione PCA
df_risultato, modello_kmeans, scaler = esegui_clustering(df_libri, n_clusters=4)

# 2. Addestriamo i modelli di regressione e otteniamo il modello lineare
modello_predittivo = addestra_modello_predizione(df_libri)

# 3. Facciamo un test stimando i prestiti per un libro inventato (anno 2021, 18.5€, 350 pag, 4.2 rating, 120 voti)
stima = prevedi_nuovo_libro(modello_predittivo, anno=2021, prezzo=18.5, pagine=350, rating=4.2, num_voti=120)
print(f"\nStima prestiti per il nuovo libro: {stima}")

# 4. Facciamo un test chiedendo al sistema di raccomandazione 3 libri simili a "Harry"
raccomanda_libri(df_libri, titolo_ricerca="Harry")