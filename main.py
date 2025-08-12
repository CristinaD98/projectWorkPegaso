
# funzione per generare casualmente i parametri da configurare che restituisce come output il tempo di produzione dell'intero lotto 

# tempo di produzione per unità
# tempo di produzione per tipologia di prodotto
# capacità massima di produzione giornaliera di prodotto
# capacità massima di produzione giornaliera complessiva

# aggiunta mia
# costo per unità basato sulla qualità dei materiali
import prodotti
import random

# Nome funzione: main
# Parametri in input: nessuno
# Valore di ritorno: tempo totale per produrre l'intero lotto (in minuti)
# Descrizione: funzione principale che fa partire il codice
def main():
    # creazione dell'istanza lotto mediante l'inserimento 
    lotto = prodotti.Lotto([generaSmartphone(), generaTelefoniAConchiglia(), generaTelefoniFissi()])
    print(lotto)
    return lotto.tempoLottoTotale


# Nome funzione: generaQuantitaProdotti
# Parametri in input: nessuno
# Valore di ritorno: valore intero
# Descrizione: funzione per generare casualmente le quantità da produrre per ogni tipo di prodotto   
def generaQuantitaProdotti():
    return random.random()*100//1
    
# Nome funzione: generaSmartphone
# Parametri in input: nessuno
# Valore di ritorno: istanza del prodotto "Smartphone"
# Descrizione: funzione per generare il tipo di prodotto corrispondente  
def generaSmartphone():
    quantita = generaQuantitaProdotti()
    telefoni = prodotti.Smartphone(quantita)
    return telefoni

# Nome funzione: generaTelefoniAConchiglia
# Parametri in input: nessuno
# Valore di ritorno: istanza del prodotto "Telefono a conchiglia"
# Descrizione: funzione per generare il tipo di prodotto corrispondente  
def generaTelefoniAConchiglia():
    quantita = generaQuantitaProdotti()
    telefoni = prodotti.Conchiglia(quantita)
    return telefoni

# Nome funzione: generaTelefoniFissi
# Parametri in input: nessuno
# Valore di ritorno: istanza del prodotto "Telefono fisso"
# Descrizione: funzione per generare il tipo di prodotto corrispondente  
def generaTelefoniFissi():
    quantita = generaQuantitaProdotti()
    telefoni = prodotti.Fisso(quantita)
    return telefoni

# chiamata alla funzione che fa partire il programma
main()
