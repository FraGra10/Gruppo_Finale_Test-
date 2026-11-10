import pandas as pd
from abc import ABC, abstractmethod
from datetime import date

df = pd.read_csv("books.csv")

Rare_books  = df[df["section"] == "Rare Books"]

df = df[df["section"] != "Rare Books"]

df = df.dropna()

df = pd.concat(
    [df, Rare_books],
    ignore_index=True
)



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
        pass

    @abstractmethod
    def prestabile(self):
        """True se il libro può uscire dalla biblioteca."""
        pass   
    
    @abstractmethod
    def costo_prestito(self,giorni_prestito):
        pass 
    
    #numero di copie del libro
    def get_numero_copie(self):
        return self.copie_totali
    
    #numero di copie in prestito del libro 
    def get_copie_in_prestito(self):
        return self.__copie_in_prestito
    
    def set_copie_in_prestito(self,data):
        self.__copie_in_prestito = data 
    
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

#    def __init__(self,titolo,autore,anno_pubblicazione,genere,sezione,copie_totali,numero_prestiti,
#                      data_ultimo_prestito, rating, rating_count, prezzo, lingua, numero_pagine,
#                      lunghezza, spessore, altezza,scaffale, riga, numero_riga):
        
#        super().__init__(titolo,autore,anno_pubblicazione,genere,sezione,copie_totali,numero_prestiti,
#                        data_ultimo_prestito, rating, rating_count, prezzo, lingua, numero_pagine,
#                        lunghezza, spessore, altezza,scaffale, riga, numero_riga)

    def costo_prestito(self,giorni_prestito):
        
        return 1/3*self.prezzo + 1*giorni_prestito
    
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
        
        self.area_tematica = sezione
        
    def costo_prestito(self,giorni_prestito):
        
        return 2/3*self.prezzo + 1*giorni_prestito
    
    def sezione_libro(self):
        print("Questo non è un libro di narrativa!")
        
    def prestabile(self):
        return True 
    
    def get_area_tematica(self):
        return self.area_tematica
                    
class ChildrenBook(Libro):

#    def __init__(self,titolo,autore,anno_pubblicazione,genere,sezione,copie_totali,numero_prestiti,
#                      data_ultimo_prestito, rating, rating_count, prezzo, lingua, numero_pagine,
#                      lunghezza, spessore, altezza,scaffale, riga, numero_riga):
        
#        super().__init__(titolo,autore,anno_pubblicazione,genere,sezione,copie_totali,numero_prestiti,
#                        data_ultimo_prestito, rating, rating_count, prezzo, lingua, numero_pagine,
#                        lunghezza, spessore, altezza,scaffale, riga, numero_riga)

    def costo_prestito(self,giorni_prestito):
        
        return 1/3*self.prezzo + 1*giorni_prestito
        
    def sezione_libro(self):
        print("Questo è un libro per bambini!")
        
    def prestabile(self):
        return True 
                    
class YoungAdultBook(Libro):

#    def __init__(self,titolo,autore,anno_pubblicazione,genere,sezione,copie_totali,numero_prestiti,
#                      data_ultimo_prestito, rating, rating_count, prezzo, lingua, numero_pagine,
#                      lunghezza, spessore, altezza,scaffale, riga, numero_riga):
        
#        super().__init__(titolo,autore,anno_pubblicazione,genere,sezione,copie_totali,numero_prestiti,
#                        data_ultimo_prestito, rating, rating_count, prezzo, lingua, numero_pagine,
#                        lunghezza, spessore, altezza,scaffale, riga, numero_riga)

    def costo_prestito(self,giorni_prestito):
        
        return 2/3*self.prezzo + 1*giorni_prestito
    
    def sezione_libro(self):
        print("Questo è un libro per ragazzi!")
        
    def prestabile(self):
        return True    
    
                 
class ReferenceBook(Libro):

#    def __init__(self,titolo,autore,anno_pubblicazione,genere,sezione,copie_totali,numero_prestiti,
#                      data_ultimo_prestito, rating, rating_count, prezzo, lingua, numero_pagine,
#                      lunghezza, spessore, altezza,scaffale, riga, numero_riga):
        
#        super().__init__(titolo,autore,anno_pubblicazione,genere,sezione,copie_totali,numero_prestiti,
#                        data_ultimo_prestito, rating, rating_count, prezzo, lingua, numero_pagine,
#                        lunghezza, spessore, altezza,scaffale, riga, numero_riga)
                
    def sezione_libro(self):
        print("Questo è un'opera di consultazione!")
    
    def prestabile(self):
        return False
    
    def costo_prestito(self,giorni_prestito):
        
        return 0 #Non è prestabile 
    
class RareBook(Libro):

#    def __init__(self,titolo,autore,anno_pubblicazione,genere,sezione,copie_totali,numero_prestiti,
#                      data_ultimo_prestito, rating, rating_count, prezzo, lingua, numero_pagine,
#                      lunghezza, spessore, altezza,scaffale, riga, numero_riga):
        
#        super().__init__(titolo,autore,anno_pubblicazione,genere,sezione,copie_totali,numero_prestiti,
#                        data_ultimo_prestito, rating, rating_count, prezzo, lingua, numero_pagine,
#                        lunghezza, spessore, altezza,scaffale, riga, numero_riga)
                
    def sezione_libro(self):
        print("Questo è un libro raro!")
    
    def prestabile(self):
        return False
    
    def costo_prestito(self,giorni_prestito):
        
        return 0 #Non è prestabile 

         
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
    
    elif(sezione[i] == "Rare Books"):
        Books_list.append(RareBook(titolo[i],autore[i],anno_pubblicazione[i],genere[i],sezione[i],copie_totali[i],numero_prestiti[i],
                      data_ultimo_prestito[i], rating[i], rating_count[i], prezzo[i], lingua[i], numero_pagine[i],
                      lunghezza[i], spessore[i], altezza[i],scaffale[i], riga[i], numero_riga[i]))

    else:
        Books_list.append(FictionBook(titolo[i],autore[i],anno_pubblicazione[i],genere[i],sezione[i],copie_totali[i],numero_prestiti[i],
                      data_ultimo_prestito[i], rating[i], rating_count[i], prezzo[i], lingua[i], numero_pagine[i],
                      lunghezza[i], spessore[i], altezza[i],scaffale[i], riga[i], numero_riga[i]))                  


#Definizione della classe biblioteca 
class Biblioteca():
    
    def __init__(self,Books_list):
        
        self.Books = Books_list
            
#Funzione per prendere in prestito un libro dalla biblioteca    
    def prendi_in_prestito(self,nome):
                
        index = -1
        for y in range(len(self.Books)):
            
            if(nome.lower() == self.Books[y].titolo.lower()):
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

#Restituisci libro prestato                   
    def restituisci_libro_prestito(self,nome, giorni_prestito):
                
        index = -1
        for y in range(len(self.Books)):
            
            if(nome.lower() == self.Books[y].titolo.lower()):
                index = y
                break 
                
        if(index == -1):
            print("Libro non trovato!")
        else:    
            if(self.Books[index].get_copie_in_prestito() > 0  ):
                print("Il prezzo da pagare è:", round(self.Books[index].costo_prestito(giorni_prestito),2) , "$" )
                self.Books[index].set_copie_in_prestito(self.Books[index].get_copie_in_prestito() - 1)
                print("Libro riconsegnato!")
            else:
                print(f"Il libro {self.Books[index].titolo} non è mai stato prestato!")


#Elenco dei libri divisi per sezione            
    def ricerca_per_sezione(self,nome_sezione):
        
        for y in range(len(self.Books)):
            if(self.Books[y].sezione.lower() == nome_sezione.lower()):
                print(self.Books[y])
                
#Elenco dei libri divisi per autore     
    def ricerca_per_autore(self,nome_autore):

        for y in range(len(self.Books)):
            if(self.Books[y].autore.lower() == nome_autore.lower()):
                print(self.Books[y])           

#Elenco dei libri divisi per genere             
    def ricerca_per_genere(self,genere):

        for y in range(len(self.Books)):
            if(self.Books[y].genere.lower() == genere.lower()):
                print(self.Books[y])

#Ricerca dei libri per titolo, scaffale e genere    
    def ricerca_per_titolo_scaffale_riga(self,titolo):
        ind =  0 
        for y in range(len(self.Books)):
            if(self.Books[y].titolo.lower() == titolo.lower()):
                print("Il libro da te cercato è: ",self.Books[y])
                print("Lo puoi trovare nello scaffale: ", self.Books[y].scaffale, "alla riga : ",self.Books[y].riga, "posizione numero: ", self.Books[y].numero_riga )
                ind = 1 
                break
        if(ind == 0):
            print("Libro non trovato!")
        
#Ordinamento dei libri per rating e stampa dei primi 100 libri                                 
    def ordinamento_per_rating(self):
        ordinati = sorted(self.Books, key=lambda libro: libro.rating, reverse=True)
        
        for libro in ordinati[:100]:
            print(libro.titolo, "-", libro.rating)

#Stampa del valore totale dei libri presenti in Biblioteca 
    def valore_totale(self):
        somma_prezzi = 0 
        for i in self.Books:
            somma_prezzi += i.prezzo*i.copie_totali
        
        print("Il valore totale dei libri presenti in Biblioteca è pari a :", round(somma_prezzi,3) , "$")





######
Bib = Biblioteca(Books_list)
#Bib.prendi_in_prestito("The Hobbit (1st Edition)")
#Bib.restituisci_libro_prestito("Harry potter and the prisoner of azkaban",15)

#Bib.ricerca_per_sezione("Rare Books")
Bib.ricerca_per_titolo_scaffale_riga("Harry potter and the prisoner of azkaban")
#Bib.ordinamento_per_rating()
#Bib.valore_totale()
    
#print(Books_list[1170].get_area_tematica())