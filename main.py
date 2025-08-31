# import delle librerie
import random
import importlib
import constants


# Nome funzione: main
# Parametri in input: nessuno
# Valore di ritorno: tempo totale per produrre l'intero lotto (in minuti)
# Descrizione: funzione principale che fa partire il codice
def main():
    # import dinamico del modulo prodotti
    moduloProdotti = importlib.import_module(constants.MODULO_PRODOTTI)
    # import mediante file delle costanti del dizionario contenente cosa inserire nel lotto
    dizionarioDiProdottiDaCreare = constants.PRODOTTI_DA_CREARE
    # inizializzazione dell'array delle istanze
    elencoIstanze = []
    # ciclo for usato per creare le singole istanze e le annesse quantità di prodotti
    for i in dizionarioDiProdottiDaCreare.keys():
        quantita = 0
        # se il tipo di prodotto è censito come "Manuale", l'utente sarà tenuto a inserire manualmente la quantità di prodotto che vuole inserire nel lotto
        if dizionarioDiProdottiDaCreare[i] == "Manuale":
            quantita = int(input("Quante unità di "+i+" si vogliono aggiungere nel lotto?\n"))
        else:
            # se invece non è manuale
            quantita = generaQuantitaProdotti()
        # Gestione manuale dell'eccezione fuoriuscita qualora nel dizionario fosse presente un prodotto che però non è stato correttamente configurato nell'apposito file
        try:
            elencoIstanze.append(getattr(moduloProdotti, i)(quantita))
        except AttributeError:
            print('\nIl prodotto',i,'non è stato configurato correttamente.')
        
    # Gestione manuale dell'eccezione fuoriuscita quando si cerca di accedere ad una variabile privata della classe
    try:
        print(elencoIstanze[0].__tempoDiProduzionePerSingolaUnita)
    except Exception as exc:
        print('\nEccezione per mostrare il risultato di un tentativo di accesso ad una variabile privata:', exc)
    # creazione dell'istanza lotto mediante l'inserimento di un array composto da n tipi di prodotti
    lotto = moduloProdotti.Lotto(elencoIstanze)
    # lotto = prodotti.Lotto([generaSmartphone(), generaTelefoniAConchiglia(), generaTelefoniFissi()])
    lotto.stampaProdottiLotto()
    lotto.calcolaTempoTotaleLotto()
    print(lotto)
    return lotto.tempoLottoTotale


# Nome funzione: generaQuantitaProdotti
# Parametri in input: nessuno
# Valore di ritorno: valore intero corrispondente al numero di prodotto specifico da generare
# Descrizione: funzione per generare casualmente le quantità da produrre per ogni tipo di prodotto   
def generaQuantitaProdotti():
    # il valore viene arrotondato per semplicità
    return int(random.random()*100)
    
# # Nome funzione: generaSmartphone
# # Parametri in input: nessuno
# # Valore di ritorno: istanza del prodotto "Smartphone"
# # Descrizione: funzione per generare il tipo di prodotto corrispondente  
# def generaSmartphone():
#     quantita = generaQuantitaProdotti()
#     # la variabile telefoni si popola con la nuova istanza della classe Smartphone contenuta nel file
#     #  prodotti.py
#     telefoni = prodotti.Smartphone(quantita)
#     # Gestione manuale dell'eccezione fuoriuscita quando si cerca di accedere ad una variabile privata della classe
#     try:
#         print(telefoni.__tempoDiProduzionePerSingolaUnita)
#     except Exception as exc:
#         print('Eccezione per mostrare il risultato di un tentativo di accesso ad una variabile privata', exc)

#     return telefoni

# # Nome funzione: generaTelefoniAConchiglia
# # Parametri in input: nessuno
# # Valore di ritorno: istanza del prodotto "Telefono a conchiglia"
# # Descrizione: funzione per generare il tipo di prodotto corrispondente  
# def generaTelefoniAConchiglia():
#     quantita = generaQuantitaProdotti()
#     # la variabile telefoni si popola con la nuova istanza della classe Conchiglia contenuta nel file prodotti.py
#     telefoni = prodotti.Conchiglia(quantita)
#     return telefoni

# # Nome funzione: generaTelefoniFissi
# # Parametri in input: nessuno
# # Valore di ritorno: istanza del prodotto "Telefono fisso"
# # Descrizione: funzione per generare il tipo di prodotto corrispondente  

# def generaTelefoniFissi():
#     quantita = generaQuantitaProdotti()
#     # la variabile telefoni si popola con la nuova istanza della classe Fisso contenuta nel file prodotti.py
#     telefoni = prodotti.Fisso(quantita)
#     return telefoni

# chiamata alla funzione che fa partire il programma
main()


