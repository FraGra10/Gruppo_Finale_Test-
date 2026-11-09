import pandas as pd




df = pd.read_csv("books.csv")
df = df.dropna()


titolo = df["title"].tolist()
autore = df["author"].tolist()
anno_pubblicazione = df["year_published"].tolist()
genere = df["genre"].tolist()
sezione = df["section"].tolist()
copie_totali = df["total_copies"].tolist()
numero_prestiti = df["times_borrowed"].tolist()
data_ultimo_prestito = df["last_borrowed_date"].tolist()
rating = df["rating"].tolist()
rating_count = df["ratings_count"].tolist()
prezzo = df["price"].tolist()
lingua = df["language"].tolist()
numero_pagine= df["page_count"].tolist()
lunghezza = df["dimensions_width"].tolist()
spessore = df["dimensions_thickness"].tolist()
altezza = df["dimensions_height"].tolist()
scaffale = df["catalog_shelf"].tolist()
riga = df["catalog_row"].tolist()
numero_riga = df["catalog_row_number"].tolist()

#definizione della classe 
class Libro:
    
    def __init__(self,titolo,autore,anno_pubblicazione,genere,sezione,copie_totali,numero_prestiti,
                      data_ultimo_prestito, rating, rating_count, prezzo, lingua, numero_pagine,
                      lunghezza, spessore, altezza,scaffale, riga, numero_riga):
        
        self.titolo = titolo
        self.autore = autore 
        self.anno_pubblicazione = anno_pubblicazione
        self.genere = genere 
        self.sezione = sezione
        self.copie_totali = copie_totali
        self.numero_prestiti = numero_prestiti
        self.data_ultimo_prestito = data_ultimo_prestito
        self.rating = rating 
        self.rating_count = rating_count
        self.prezzo = prezzo 
        self.lingua = lingua
        self.numero_pagine = numero_pagine
        self.lunghezza = lunghezza 
        self.spessore = spessore 
        self.altezza = altezza 
        self.scaffale = scaffale 
        self.riga = riga 
        self.numero_riga = numero_riga 
        

#definizione delle classi figlie        
class FictionBook(Libro):

    def __init__(self,titolo,autore,anno_pubblicazione,genere,sezione,copie_totali,numero_prestiti,
                      data_ultimo_prestito, rating, rating_count, prezzo, lingua, numero_pagine,
                      lunghezza, spessore, altezza,scaffale, riga, numero_riga):
        
        super().__init__(titolo,autore,anno_pubblicazione,genere,sezione,copie_totali,numero_prestiti,
                        data_ultimo_prestito, rating, rating_count, prezzo, lingua, numero_pagine,
                        lunghezza, spessore, altezza,scaffale, riga, numero_riga)

class NonFictionBook(Libro):

    def __init__(self,titolo,autore,anno_pubblicazione,genere,sezione,copie_totali,numero_prestiti,
                      data_ultimo_prestito, rating, rating_count, prezzo, lingua, numero_pagine,
                      lunghezza, spessore, altezza,scaffale, riga, numero_riga):
        
        super().__init__(titolo,autore,anno_pubblicazione,genere,sezione,copie_totali,numero_prestiti,
                        data_ultimo_prestito, rating, rating_count, prezzo, lingua, numero_pagine,
                        lunghezza, spessore, altezza,scaffale, riga, numero_riga)
        
class ChildrenBook(Libro):

    def __init__(self,titolo,autore,anno_pubblicazione,genere,sezione,copie_totali,numero_prestiti,
                      data_ultimo_prestito, rating, rating_count, prezzo, lingua, numero_pagine,
                      lunghezza, spessore, altezza,scaffale, riga, numero_riga):
        
        super().__init__(titolo,autore,anno_pubblicazione,genere,sezione,copie_totali,numero_prestiti,
                        data_ultimo_prestito, rating, rating_count, prezzo, lingua, numero_pagine,
                        lunghezza, spessore, altezza,scaffale, riga, numero_riga)
        
class YoungAdultBook(Libro):

    def __init__(self,titolo,autore,anno_pubblicazione,genere,sezione,copie_totali,numero_prestiti,
                      data_ultimo_prestito, rating, rating_count, prezzo, lingua, numero_pagine,
                      lunghezza, spessore, altezza,scaffale, riga, numero_riga):
        
        super().__init__(titolo,autore,anno_pubblicazione,genere,sezione,copie_totali,numero_prestiti,
                        data_ultimo_prestito, rating, rating_count, prezzo, lingua, numero_pagine,
                        lunghezza, spessore, altezza,scaffale, riga, numero_riga)
        
class ReferenceBook(Libro):

    def __init__(self,titolo,autore,anno_pubblicazione,genere,sezione,copie_totali,numero_prestiti,
                      data_ultimo_prestito, rating, rating_count, prezzo, lingua, numero_pagine,
                      lunghezza, spessore, altezza,scaffale, riga, numero_riga):
        
        super().__init__(titolo,autore,anno_pubblicazione,genere,sezione,copie_totali,numero_prestiti,
                        data_ultimo_prestito, rating, rating_count, prezzo, lingua, numero_pagine,
                        lunghezza, spessore, altezza,scaffale, riga, numero_riga)
                

#Creazione dell'istanza del libro in base alla categoria di appartenenza 
Books_list = []


for i in range(len(titolo)):
    
    if(sezione[i] == "Young Adult" or sezione[i] == "Young Adult (YA)"):
        Books_list.append(YoungAdultBook(titolo[i],autore[i],anno_pubblicazione[i],genere[i],sezione[i],copie_totali[i],numero_prestiti[i],
                      data_ultimo_prestito[i], rating[i], rating_count[i], prezzo[i], lingua[i], numero_pagine[i],
                      lunghezza[i], spessore[i], altezza[i],scaffale[i], riga[i], numero_riga[i]))
    
    elif(sezione[i] == "Reference"):
        Books_list.append(ReferenceBook(titolo[i],autore[i],anno_pubblicazione[i],genere[i],sezione[i],copie_totali[i],numero_prestiti[i],
                      data_ultimo_prestito[i], rating[i], rating_count[i], prezzo[i], lingua[i], numero_pagine[i],
                      lunghezza[i], spessore[i], altezza[i],scaffale[i], riga[i], numero_riga[i]))  
                
    elif(sezione[i] == "Children" or sezione[i] == "Children's" or sezione[i] == "Children's Fiction"):
        Books_list.append(ChildrenBook(titolo[i],autore[i],anno_pubblicazione[i],genere[i],sezione[i],copie_totali[i],numero_prestiti[i],
                      data_ultimo_prestito[i], rating[i], rating_count[i], prezzo[i], lingua[i], numero_pagine[i],
                      lunghezza[i], spessore[i], altezza[i],scaffale[i], riga[i], numero_riga[i]))
        
    elif(sezione[i] == "Non-Fiction" or sezione[i] == "Humanities" or sezione[i] == "History" or sezione[i] == "Science"):
        Books_list.append(NonFictionBook(titolo[i],autore[i],anno_pubblicazione[i],genere[i],sezione[i],copie_totali[i],numero_prestiti[i],
                      data_ultimo_prestito[i], rating[i], rating_count[i], prezzo[i], lingua[i], numero_pagine[i],
                      lunghezza[i], spessore[i], altezza[i],scaffale[i], riga[i], numero_riga[i]))
    
    else:
        Books_list.append(FictionBook(titolo[i],autore[i],anno_pubblicazione[i],genere[i],sezione[i],copie_totali[i],numero_prestiti[i],
                      data_ultimo_prestito[i], rating[i], rating_count[i], prezzo[i], lingua[i], numero_pagine[i],
                      lunghezza[i], spessore[i], altezza[i],scaffale[i], riga[i], numero_riga[i]))                 


