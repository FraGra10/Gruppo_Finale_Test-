import pandas as pd
from abc import ABC, abstractmethod
from datetime import date


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
class Libro(ABC):
    
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
        self.__copie_in_prestito = 0 
    
    #metodi astratti da ridefinire nelle classi figlie    
    @abstractmethod
    def sezione_libro(self):
        print("Questo è un libro!")

    @abstractmethod
    def prestabile(self):
        """True se il libro può uscire dalla biblioteca."""
        pass   
    
    #numero di copie del libro
    def get_numero_copie(self):
        return self.copie_totali
    
    #numero di copie in prestito del libro 
    def get_copie_in_prestito(self):
        return self.__copie_in_prestito
    
    #registrazione di un prestito 
    def registra_prestito(self):
        self.__copie_in_prestito += 1
        self.data_ultimo_prestito = date.today().strftime("%m/%d/%Y")
    
    # get delle copie ancora disponibili
    def get_copie_disponibili(self):
                    
        return self.copie_totali - self.__copie_in_prestito

    #print associato alla classe
    def __str__(self):
        return f"{self.titolo} di {self.autore} ({int(self.anno_pubblicazione)}) - Sezione: {self.sezione}"
           

#definizione delle classi figlie rappresentanti le cinque sezioni         
class FictionBook(Libro):

    def __init__(self,titolo,autore,anno_pubblicazione,genere,sezione,copie_totali,numero_prestiti,
                      data_ultimo_prestito, rating, rating_count, prezzo, lingua, numero_pagine,
                      lunghezza, spessore, altezza,scaffale, riga, numero_riga):
        
        super().__init__(titolo,autore,anno_pubblicazione,genere,sezione,copie_totali,numero_prestiti,
                        data_ultimo_prestito, rating, rating_count, prezzo, lingua, numero_pagine,
                        lunghezza, spessore, altezza,scaffale, riga, numero_riga)
    
    def sezione_libro(self):
        print("Questo è un libro di narrativa!")
        
    def prestabile(self):
        return True 
             
class NonFictionBook(Libro):

    def __init__(self,titolo,autore,anno_pubblicazione,genere,sezione,copie_totali,numero_prestiti,
                      data_ultimo_prestito, rating, rating_count, prezzo, lingua, numero_pagine,
                      lunghezza, spessore, altezza,scaffale, riga, numero_riga):
        
        super().__init__(titolo,autore,anno_pubblicazione,genere,sezione,copie_totali,numero_prestiti,
                        data_ultimo_prestito, rating, rating_count, prezzo, lingua, numero_pagine,
                        lunghezza, spessore, altezza,scaffale, riga, numero_riga)
        
    def sezione_libro(self):
        print("Questo non è un libro di narrativa!")
        
    def prestabile(self):
        return True 
                    
class ChildrenBook(Libro):

    def __init__(self,titolo,autore,anno_pubblicazione,genere,sezione,copie_totali,numero_prestiti,
                      data_ultimo_prestito, rating, rating_count, prezzo, lingua, numero_pagine,
                      lunghezza, spessore, altezza,scaffale, riga, numero_riga):
        
        super().__init__(titolo,autore,anno_pubblicazione,genere,sezione,copie_totali,numero_prestiti,
                        data_ultimo_prestito, rating, rating_count, prezzo, lingua, numero_pagine,
                        lunghezza, spessore, altezza,scaffale, riga, numero_riga)
    
    def sezione_libro(self):
        print("Questo è un libro per bambini!")
        
    def prestabile(self):
        return True 
                    
class YoungAdultBook(Libro):

    def __init__(self,titolo,autore,anno_pubblicazione,genere,sezione,copie_totali,numero_prestiti,
                      data_ultimo_prestito, rating, rating_count, prezzo, lingua, numero_pagine,
                      lunghezza, spessore, altezza,scaffale, riga, numero_riga):
        
        super().__init__(titolo,autore,anno_pubblicazione,genere,sezione,copie_totali,numero_prestiti,
                        data_ultimo_prestito, rating, rating_count, prezzo, lingua, numero_pagine,
                        lunghezza, spessore, altezza,scaffale, riga, numero_riga)
    
    def sezione_libro(self):
        print("Questo è un libro per adulti!")
        
    def prestabile(self):
        return True    
    
                 
class ReferenceBook(Libro):

    def __init__(self,titolo,autore,anno_pubblicazione,genere,sezione,copie_totali,numero_prestiti,
                      data_ultimo_prestito, rating, rating_count, prezzo, lingua, numero_pagine,
                      lunghezza, spessore, altezza,scaffale, riga, numero_riga):
        
        super().__init__(titolo,autore,anno_pubblicazione,genere,sezione,copie_totali,numero_prestiti,
                        data_ultimo_prestito, rating, rating_count, prezzo, lingua, numero_pagine,
                        lunghezza, spessore, altezza,scaffale, riga, numero_riga)
                
    def sezione_libro(self):
        print("Questo è un'opera di consultazione!")
    
    def prestabile(self):
        return False         
#Creazione dell'istanza del libro in base alla categoria di appartenenza 
#Aggiunta delle istanze del libro ad un'unica lista 
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



class Biblioteca():
    
    def __init__(self,Books_list):
        
        self.Books = Books_list
        
    
    def prendi_in_prestito(self,nome):
                
        index = -1
        for y in range(len(self.Books)):
            
            if(nome == self.Books[y].titolo):
                index = y
                break 
                
        if(index == -1):
            print("Libro non trovato!")
        else:
            print("Libro trovato!")
            print("Il libro da te cercato è :", self.Books[index])
            
            if(self.Books[index].prestabile() and  self.Books[index].get_copie_disponibili() > 0 ):
                print("Il libro può essere preso in prestito!")
                self.Books[index].registra_prestito()
            else:
                print("Il libro non può essere prestato!")
                if( not self.Books[index].prestabile()):
                    print("Questo libro è solo per consultazione!")
                else:
                    print("Le copie del libro sono finite!")
            
    def ricerca_per_sezione(self,nome_sezione):
        
        for y in range(len(self.Books)):
            if(self.Books[y].sezione == nome_sezione):
                print(self.Books[y])
                
    
    def ricerca_per_autore(self,nome_autore):

        for y in range(len(self.Books)):
            if(self.Books[y].autore == nome_autore):
                print(self.Books[y])           
            
    def ricerca_per_genere(self,genere):

        for y in range(len(self.Books)):
            if(self.Books[y].genere == genere):
                print(self.Books[y])
    
    def ricerca_per_titolo_scaffale_riga(self,titolo):
        
        for y in range(len(self.Books)):
            if(self.Books[y].titolo == titolo):
                print("Il libro da te cercato è: ",self.Books[y])
                print("Lo puoi trovare allo scaffale: ", self.Books[y].scaffale, "alla riga : ",self.Books[y].riga, " alla posizione numero: ", self.Books[y].numero_riga )
                               
    def ordinamento_per_rating(self):
        
        for y in range(len(self.Books)):
            print(self.Books[y].rating)

Bib = Biblioteca(Books_list)
#Bib.prendi_in_prestito()

#Bib.ricerca_per_sezione("Reference")
#Bib.ricerca_per_titolo_scaffale_riga("Catching Fire")
Bib.ordinamento_rating()
    
