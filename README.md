<div align="center">

# 📚 Intelligent Library System
### Sistema Integrato di Gestione, Analisi Dati e Machine Learning per Biblioteche

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine_Learning-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-Interactive_Charts-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)

*Progetto Finale realizzato dal gruppo **I BIBLIOTECARI** — Alessandro Moceri, Alessia Mori, Davide Fioretti, Francesco Grasso*

</div>

---

## 📑 Indice
1. [Descrizione e Obiettivi del Progetto](#-descrizione-e-obiettivi-del-progetto)
2. [Architettura del Sistema](#-architettura-del-sistema)
3. [Moduli e Funzionalità](#-moduli-e-funzionalità)
   - [Modulo 1: Programmazione ad Oggetti (OOP)](#1-modulo-oop-biblioteca_ooppy)
   - [Modulo 2: Analisi Esplorativa dei Dati (EDA)](#2-modulo-analisi-dati-analisibibliotecadfpy)
   - [Modulo 3: Machine Learning & Sistemi Predittivi](#3-modulo-machine-learning-mlbibliotecapy)
4. [Risultati Sperimentali e Grafici](#-risultati-sperimentali-e-grafici)
5. [Installazione ed Esecuzione](#-installazione-ed-esecuzione)
6. [Struttura della Repository](#-struttura-della-repository)

---

## 🎯 Descrizione e Obiettivi del Progetto

**Intelligent Library System** è un'applicazione modulare sviluppata in Python progettata per trasformare la gestione tradizionale di una biblioteca in un ecosistema *data-driven*. 

Il software copre l'intero ciclo di vita del dato:
* **Gestione Operativa:** Modellazione ad oggetti del catalogo, dei prestiti, delle restituzioni e della collocazione fisica sugli scaffali.
* **Business Intelligence & EDA:** Pulizia del dataset (`books.csv`) e visualizzazione statistica tramite grafici statici e interattivi.
* **Intelligenza Artificiale:** Segmentazione automatica dei volumi, previsione dei prestiti futuri per ottimizzare gli acquisti e motore di raccomandazione per gli utenti.

---

## 🏗️ Architettura del Sistema

Il software segue un'architettura modulare coordinata da un'interfaccia a riga di comando (`menu.py`), che disaccoppia la navigazione utente dalla logica computazionale:

```mermaid
graph TD
    A[🖥️ menu.py <br/> Controller Principale CLI] --> B[📘 Biblioteca_OOP.py <br/> Gestione Catalogo & Classi]
    A --> C[📊 analisiBibliotecaDF.py <br/> Pulizia & Grafici EDA]
    A --> D[🤖 mlbiblioteca.py <br/> Clustering, Regressione & RecSys]
    
    E[(📂 books.csv)] --> B
    E --> C
    C -->|DataFrame Pulito| D
    D -->|Export| F[📄 libri_con_cluster.csv]
    D -->|Export| G[🖼️ grafico_cluster_pca.png]
