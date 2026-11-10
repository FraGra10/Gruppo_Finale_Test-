import pandas as pd
import matplotlib.pyplot as plt

# 1. Carichiamo e puliamo il dataframe a livello generale del modulo
df = pd.read_csv('books.csv')

# FUNZIONI RICHIAMATE DAL MENU

def esplora_dataframe():
    """Mostra le informazioni e statistiche iniziali del DataFrame."""
    print("--- SHAPE DEL DATAFRAME ---")
    print(df.shape)  # forma del df (righe x colonne)
    
    print('\n---------------------------------')
    print("--- INFO DEL DATAFRAME ---")
    print(df.info())
    
    print('\n---------------------------------')
    print("--- STATISTICHE (DESCRIBE) ---")
    print(df.describe())
    
    print('\n---------------------------------')
    print("--- PRIME 8 RIGHE (HEAD) ---")
    print(df.head(8))


def pulisci_dataset():
    """Elimina i duplicati e le righe con valori nulli."""
    global df
    df = df.drop_duplicates()
    df = df.dropna()
    print("\nDataset pulito con successo! (Rimossi duplicati e valori nulli)")
    print(df.info())


def mostra_grafico_torta():
    """Genera il grafico a torta dei Top 10 generi più presi in prestito."""
    # Raggruppo per genere e sommo per i prestiti
    prestiti_per_genere = df.groupby("genre")["times_borrowed"].sum()
    prestiti_per_genere_top_ten = prestiti_per_genere.sort_values(ascending=False).head(10)

    plt.figure(figsize=(6, 6))
    plt.pie(
        prestiti_per_genere_top_ten,
        labels=prestiti_per_genere_top_ten.index,
        autopct="%1.1f%%", 
        colors=plt.cm.Set3.colors,
    )
    plt.title("La Top Ten dei prestiti dei generi più apprezzati")
    plt.show()


def mostra_grafico_barre():
    """Genera il grafico a barre orizzontali dei 10 libri più prestati."""
    top_10 = df.sort_values("times_borrowed", ascending=False).head(10)
    etichette = top_10["title"] + " — " + top_10["author"]

    fig, ax = plt.subplots(figsize=(11, 6))
    ax.barh(etichette, top_10["times_borrowed"], color=plt.cm.Set3.colors)
    ax.invert_yaxis()
    ax.set_xlabel("Numero di prestiti")
    ax.set_title("I 10 libri più prestati")
    fig.tight_layout()
    plt.show()


def mostra_grafico_mesi():
    """Genera il grafico a barre per i prestiti divisi per mese."""
    date = pd.to_datetime(df["last_borrowed_date"], format="%m/%d/%Y")
    libri_per_mese = date.dt.to_period("M").value_counts().sort_index()

    plt.figure(figsize=(8, 4))
    plt.bar(libri_per_mese.index.astype(str), libri_per_mese, color=plt.cm.Set3.colors)
    plt.title("Libri per mese dell’ultimo prestito")
    plt.xlabel("Mese")
    plt.ylabel("Numero di libri")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()