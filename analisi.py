import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Caricamento del dataset
df = pd.read_csv('books.csv')


def esplora_dataframe():
    """Mostra le informazioni e statistiche iniziali del DataFrame."""
    print("\n--- SHAPE DEL DATAFRAME ---")
    print(df.shape)  # Forma del df (righe x colonne)
    
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
    """Effettua la pulizia del dataset: uniforma le sezioni, rimuove duplicati e valori nulli."""
    global df
    # Sostituzione variante nome sezione
    df["section"] = df["section"].replace({"Young Adult (YA)": "Young Adult"})
    
    # Rimozione duplicati e righe con valori mancanti
    df = df.drop_duplicates()
    df = df.dropna()
    
    print("\n[OK] Dataset pulito con successo!")
    print(df.info())


def mostra_grafico_torta():
    """Genera il grafico a torta dei Top 10 generi più presi in prestito (Matplotlib)."""
    prestiti_per_genere = df.groupby("genre")["times_borrowed"].sum()
    prestiti_per_genere_top_ten = prestiti_per_genere.sort_values(ascending=False).head(10)

    plt.figure(figsize=(6, 6))
    plt.pie(
        prestiti_per_genere_top_ten,
        labels=prestiti_per_genere_top_ten.index,
        autopct="%.2f%%", 
        colors=plt.cm.Set3.colors,
    )
    plt.title("La top Ten dei prestiti dei generi più apprezzati")
    plt.tight_layout()
    plt.show()


def mostra_grafico_barre_top10():
    """Genera il grafico a barre orizzontali dei 10 libri più prestati (Matplotlib)."""
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
    """Genera il grafico a barre per i prestiti divisi per mese (Matplotlib)."""
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


def mostra_scatter_plotly():
    """Genera lo Scatter Plot interattivo (Valutazione vs Prestiti) tramite Plotly."""
    fig = px.scatter(
        df,
        x="rating",
        y="times_borrowed",
        color="section",
        hover_name="title",
        hover_data=["author", "genre", "ratings_count"],
        color_discrete_sequence=px.colors.qualitative.Vivid,
        labels={
            "rating": "Valutazione media",
            "times_borrowed": "Numero di prestiti",
            "section": "Sezione",
            "author": "Autore",
            "genre": "Genere",
            "ratings_count": "Numero di valutazioni",
        },
        title="Valutazioni e prestiti dei libri (Scatter Plot Interattivo)",
    )
    fig.show()


def mostra_prestiti_medi_plotly():
    """Genera il grafico a barre della media prestiti per sezione tramite Plotly."""
    prestiti_medi = (
        df.groupby("section", as_index=False)["times_borrowed"]
        .mean()
        .sort_values("times_borrowed", ascending=False)
    )

    fig = px.bar(
        prestiti_medi,
        x="times_borrowed",
        y="section",
        color="section",
        color_discrete_sequence=px.colors.qualitative.Set3,
        text_auto=".0f",
        labels={
            "times_borrowed": "Prestiti medi per libro",
            "section": "Sezione",
        },
        title="Media dei prestiti per sezione (Plotly)",
    )
    fig.update_xaxes(hoverformat=".0f")
    fig.show()