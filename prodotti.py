# import delle librerie
import random
import constants

# Nome funzione: definisciComplessitaProdotto
# Parametri in input: nessuno
# Valore di ritorno: valore intero
# Descrizione: funzione utilizzata per generare casualmente il livello di complessità del prodotto
# Generalmente questo tipo di operazione sarebbe effettuato in fase di analisi dal gruppo che si occupa
# di studiare i vari componenti e materiali. In questo caso la funzione è stata implementata
# per evidenziare come la complessità del prodotto influisce sulle tempistiche di produzione dello stesso
def definisciComplessitaProdotto():
    return int(random.uniform(1.0, 4.0))

# Nome funzione: tempoDiProduzioneOrario
# Parametri in input: nessuno
# Valore di ritorno: valore intero
# Descrizione: funzione utilizzata per generare casualmente il numero di minuti impiegati per la produzione
# del singolo tipo di prodotto. Anche in questo caso, in una processo produttivo non simulato, il tempo di
# produzione di un singolo tipo di prodotto sarebbe calcolato in fase di analisi in base ad un elenco di molteplici
# fattori, come per esempio la necessità dell'impiego di robot, il numero e la disponibilità degli stessi, 
# la presenza o no di intervento umano, etc
def tempoDiProduzioneOrario():
    return int(random.uniform(1.0, constants.NUMERO_TOTALE_MINUTI_IN_ORA))


# Nome funzione: calcoloCostoMateriali
# Parametri in input: soglia di prezzo minima (int) e soglia di prezzo massima (int)
# Valore di ritorno: valore float arrotondato a due cifre decimali
# Descrizione: funzione utilizzata per generare casualmente il prezzo dei materiali spesi per produrre 
# la singola unità di prodotto
def calcoloCostoMateriali(modificatoreTipoDiProdottoMin,modificatoreTipoDiProdottoMax):
    return round(random.uniform(modificatoreTipoDiProdottoMin, modificatoreTipoDiProdottoMax),2)

# Nome funzione: calcoloTempoTotale
# Parametri in input: tempoTotale in minuti
# Descrizione: funzione utilizzata per calcolare il numero di giorni, il numero di ore e il numero di minuti a partire dal tempo totale in minuti
# preso in input
def calcoloTempoTotale(tempoTotale):
    numeroGiorni = tempoTotale//constants.NUMERO_TOTALE_MINUTI_IN_GIORNO
    numeroOre = tempoTotale%constants.NUMERO_TOTALE_MINUTI_IN_GIORNO//constants.NUMERO_TOTALE_MINUTI_IN_ORA
    numeroMinuti = tempoTotale%constants.NUMERO_TOTALE_MINUTI_IN_ORA
    return numeroGiorni, numeroOre, numeroMinuti

# Nome funzione: formattazioneStringaTempistiche
# Parametri in input: tempoTotale in minuti
# Descrizione: funzione utilizzata per calcolare il numero di giorni, il numero di ore e il numero di minuti a partire dal tempo totale in minuti
# preso in input
def formattazioneStringaTempistiche(tempoTotale):
    numeroGiorni, numeroOre, numeroMinuti = calcoloTempoTotale(tempoTotale)
    return (str(numeroGiorni)+(" giorno, " if numeroGiorni ==1 else " giorni, ") if numeroGiorni !=0 else "")+str(numeroOre)+(" ora e " if numeroOre ==1 else " ore e ")+str(numeroMinuti)+ (" minuto" if numeroMinuti ==1 else " minuti")

# Nome funzione: formattazioneStringaPerStampaValori
# Parametri in input: dizionario contenente l'elenco dei tipi di prodotti con l'annessa quantità di ogni singolo prodotto
# Descrizione: funzione utilizzata per formattare meglio l'elenco dei prodotti e rendere il resoconto finale più leggibile
def formattazioneStringaPerStampaValori(dizionarioQuantita):
    stringaFinale = ""
    # il dizionario viene iterato per concatenare il tipo di prodotto, la sua quantità e eventuali stringhe aggiuntive 
    # (tra cui la virgola)
    for i in dizionarioQuantita.keys():
        stringaFinale += str(dizionarioQuantita[i])+" unità del prodotto \""+ str(i)+"\","
    # la stringaFinale così composta viene decurtata della virgola finale 
    stringaFinale = stringaFinale[:-1]

    # la stringa finale subisce un'ulteriore lavorazione per ottenere un elenco di sotto-stringhe 
    elementi = stringaFinale.split(',')
    # se la stringa ha più di due valori vuol dire che è possibile inserire la "e" al posto della virgola per una migliore lettura
    ultimo_elemento = elementi.pop()
    stringaFinale = ", ".join(elementi) + " e " + ultimo_elemento

    return stringaFinale


# Nome classe: Prodotto
# Descrizione: classe genitore utilizzata per definire dei calcoli base utilizzabili da tutti i prodotti e mostrare la
# scheda del prodotto 
class Prodotto:
    
    # Nome metodo: costruttore della classe Prodotto
    # Parametri in input: istanza attuale della classe prodotto (oggetto), numero di prodotti da creare (int), il tempo di produzione della singola unità del prodotto (int), 
    # la complessità del tipo di prodotto (int), il tipo di prodotto da creare (str) e il costo dei materiali (float)
    # Descrizione: costruttore della classe Prodotto, utilizzato per incapsulare i dati che saranno poi utilizzati per calcolare il tempo
    # di produzione del lotto 
    def __init__(self,quantita,tempoDiProduzionePerSingolaUnita,complessitaDiProduzioneDelProdotto,tipoDiProdotto,costoMaterialiProdotto):
        self.quantita = quantita
        self.tempoDiProduzionePerSingolaUnitaConComplessita = tempoDiProduzionePerSingolaUnita*complessitaDiProduzioneDelProdotto
        self.complessitaDiProduzioneDelProdotto = complessitaDiProduzioneDelProdotto
        self.costoMaterialiProdotto = costoMaterialiProdotto
        self.__tipoDiProdotto = tipoDiProdotto

    # Nome metodo: getCapacitaMassimaGiornalieraUnita
    # Parametri in input: istanza attuale della classe prodotto (oggetto)
    # Descrizione: metodo utilizzato per ottenere il numero massimo di unità producibili in un giorno.             
    def getCapacitaMassimaGiornalieraUnita(self):
        return constants.NUMERO_TOTALE_MINUTI_IN_GIORNO//self.tempoDiProduzionePerSingolaUnitaConComplessita

    # Nome metodo: getTempodiProduzioneTotale
    # Parametri in input: istanza attuale della classe prodotto (oggetto)
    # Descrizione: metodo utilizzato per ottenere il tempo di produzione di tutti i prodotti del singolo tipo  
    def getTempodiProduzioneTotale(self):
        return self.tempoDiProduzionePerSingolaUnitaConComplessita*self.quantita
    
    # Nome metodo: __str__
    # Parametri in input: istanza attuale della classe prodotto (oggetto)
    # Descrizione: metodo utilizzato per mostrare a video la scheda del prodotto     
    def __str__(self):
        return constants.ASTERISCHI+"\nTipo di prodotto: "+ str(self.__tipoDiProdotto)+"\nQuantità in produzione: "+str(int(self.quantita))+"\nComplessità di creazione del tipo di prodotto: "+str(self.complessitaDiProduzioneDelProdotto)+"\nCosto dei materiali per il tipo di prodotto: "+str(self.costoMaterialiProdotto)+constants.VALUTA+"\nTempo di produzione per singola unità: "+str(self.tempoDiProduzionePerSingolaUnitaConComplessita)+" minuti\nTempo di produzione di tutte le unità: "+formattazioneStringaTempistiche(self.getTempodiProduzioneTotale())+"\nCapacità massima giornaliera di produzione della singola unità: "+str(self.getCapacitaMassimaGiornalieraUnita())+" unità/giorno\n"+constants.ASTERISCHI

# Nome classe: Smartphone
# Descrizione: classe prodotto specifico utilizzata per definire la scheda del prodotto 
class Smartphone(Prodotto):
    tipoDiProdotto = constants.SMARTPHONE
    __tempoDiProduzionePerSingolaUnita = tempoDiProduzioneOrario()
    __complessitaDiProduzioneDelProdotto = definisciComplessitaProdotto()
    __costoMaterialiProdotto = calcoloCostoMateriali(100,200)
    # Nome metodo: costruttore della classe Smartphone
    # Parametri in input: istanza attuale della classe prodotto (oggetto), 
    # numero di prodotti da creare (int), il tempo di produzione della singola unità del prodotto (int), 
    # la complessità del tipo di prodotto (int) e il tipo di prodotto da creare (str)
    # Descrizione: costruttore della classe Smartphone, usato per passare le caratteristiche del tipo di
    # prodotto alla classe genitrice di produzione del lotto 
    def __init__(self, quantita):
        super().__init__(quantita,
                         self.__tempoDiProduzionePerSingolaUnita,
                         self.__complessitaDiProduzioneDelProdotto, 
                         self.tipoDiProdotto, 
                         self.__costoMaterialiProdotto)
    
# Nome classe: Conchiglia
# Descrizione: classe prodotto specifico utilizzata per definire la scheda del prodotto    
class Conchiglia(Prodotto):
    tipoDiProdotto = constants.TELEFONO_A_CONCHIGLIA
    __tempoDiProduzionePerSingolaUnita = tempoDiProduzioneOrario()
    __complessitaDiProduzioneDelProdotto = definisciComplessitaProdotto()
    __costoMaterialiProdotto = calcoloCostoMateriali(70,100)

    # Nome metodo: costruttore della classe Conchiglia
    # Parametri in input: istanza attuale della classe prodotto (oggetto), numero di prodotti da creare (int), il tempo di produzione della singola unità del prodotto (int), 
    # la complessità del tipo di prodotto (int) e il tipo di prodotto da creare (str)
    # Descrizione: costruttore della classe Conchiglia, usato per passare le caratteristiche del tipo di prodotto alla classe genitrice
    # di produzione del lotto
    def __init__(self, quantita):
        super().__init__(quantita,self.__tempoDiProduzionePerSingolaUnita,self.__complessitaDiProduzioneDelProdotto, self.tipoDiProdotto, self.__costoMaterialiProdotto)
    
# Nome classe: Fisso
# Descrizione: classe prodotto specifico utilizzata per definire la scheda del prodotto        
class Fisso(Prodotto):
    tipoDiProdotto = constants.FISSO
    __tempoDiProduzionePerSingolaUnita = tempoDiProduzioneOrario()
    __complessitaDiProduzioneDelProdotto = definisciComplessitaProdotto()
    __costoMaterialiProdotto = calcoloCostoMateriali(50,70)

    # Nome metodo: costruttore della classe Fisso
    # Parametri in input: istanza attuale della classe prodotto (oggetto), numero di prodotti da creare (int), il tempo di produzione della singola unità del prodotto (int), 
    # la complessità del tipo di prodotto (int) e il tipo di prodotto da creare (str)
    # Descrizione: costruttore della classe Fisso, usato per passare le caratteristiche del tipo di prodotto alla classe genitrice
    # di produzione del lotto
    def __init__(self, quantita):
        super().__init__(quantita,self.__tempoDiProduzionePerSingolaUnita,self.__complessitaDiProduzioneDelProdotto, self.tipoDiProdotto, self.__costoMaterialiProdotto)

# Nome classe: Lotto
# Descrizione: classe utilizzata per definire le caratteristiche del lotto di produzione            
class Lotto:
    tempoLottoParziale = 0
    tempoLottoTotale = 0

    # Nome metodo: costruttore della classe Lotto
    # Parametri in input: istanza attuale della classe lotto (oggetto), elenco di prodotti (lista)
    # Descrizione: costruttore della classe Lotto utilizzato per salvare nell'istanza corrente della classe i prodotti specificati in fase di inizializzazione
    def __init__(self, prodotti):
        self.prodotti = prodotti

    # Nome metodo: stampaProdottiLotto
    # Parametri in input: istanza attuale della classe lotto (oggetto)
    # Descrizione: costruttore della classe Lotto utilizzato per mostrare il resoconto dei prodotti del lotto
    # e calcolare il tempo totale di produzione
    def stampaProdottiLotto(self):
        for i in self.prodotti:
            print(i)

    # Nome metodo: calcolaTempoTotaleLotto
    # Parametri in input: istanza attuale della classe lotto (oggetto)
    # Descrizione: metodo utilizzato per calcolare il tempo totale di creazione del lotto
    def calcolaTempoTotaleLotto(self):
        tempoLottoTotale = 0
        for i in self.prodotti:
            if(i.quantita>0):
                # per calcolare la variabile tempoLottoTotale viene utilizzato un metodo presente nella classe genitrice
                # Prodotto, presente in ogni istanza di prodotto singolo
                tempoLottoTotale += i.getTempodiProduzioneTotale()
        
        # il tempo totale viene formattato per semplicità
        tempoLottoTotale = int(tempoLottoTotale)    
            
        self.tempoLottoTotale = tempoLottoTotale
        
   
    # Nome metodo: getDizionarioProduzioneMassimaGiornaliera
    # Parametri in input: istanza attuale della classe lotto (oggetto)
    # Descrizione: metodo per ottenere un dizionario di prodotti producibili in un giorno 
    def getDizionarioProduzioneMassimaGiornaliera(self):
        # inizializzazione dizionari e variabili
        dizionarioParziale = {}
        dizionarioProduzioneMassimaRaggiunta = {}
        contatoreMinutiGiornalieri = 0
        minutiGiornalieriSuperati = False
        # l'elenco dei prodotti viene iterato per sommare il tempo di produzione di tutti i prodotti
        for i in self.prodotti:
            contatoreMinutiGiornalieri += i.getTempodiProduzioneTotale()

        # se la produzione è fattibile in un giorno posso restituire l'intero lotto 
        if(contatoreMinutiGiornalieri>constants.NUMERO_TOTALE_MINUTI_IN_GIORNO):
            contatoreMinutiGiornalieri = 0
            # se la produzione totale non è fattibile in un giorno, cerco di ottenere un dizionario che contiene
            # più prodotti possibili di ogni tipo
            while contatoreMinutiGiornalieri<=constants.NUMERO_TOTALE_MINUTI_IN_GIORNO and (not minutiGiornalieriSuperati):

                for i in self.prodotti:
                    # il tipo di prodotto corrente nel dizionarioParziale viene inizializzato a 0 se assente,
                    # altrimenti prende il valore corrente
                    dizionarioParziale[i.tipoDiProdotto] = dizionarioParziale[i.tipoDiProdotto] if i.tipoDiProdotto in dizionarioParziale else 0
                    # il prodotto viene inserito nel dizionario se non tutte le quantita dello stesso sono state aggiunte al dizionario parziale e 
                    # se il tempo di produzione del singolo prodotto non eccede il tempo giornaliero di produzione 
                    if ((dizionarioParziale[i.tipoDiProdotto]<i.quantita) and 
                        (not (i.tipoDiProdotto in dizionarioProduzioneMassimaRaggiunta)) and (contatoreMinutiGiornalieri+i.tempoDiProduzionePerSingolaUnitaConComplessita<=constants.NUMERO_TOTALE_MINUTI_IN_GIORNO)):
                            # se il prodotto può essere aggiunto in quanto il tempo di produzione attuale non supera le 24h allora il 
                            # dizionarioParziale viene aggiornato con la nuova quantità
                            contatoreMinutiGiornalieri += i.tempoDiProduzionePerSingolaUnitaConComplessita
                            dizionarioParziale[i.tipoDiProdotto]+=1
                    else:
                        # il prodotto corrente viene inserito nel dizionario di produzione massima raggiunta per impedirne un'ulteriore produzione
                        dizionarioProduzioneMassimaRaggiunta[i.tipoDiProdotto]=True
                # il seguente controllo viene utilizzato per uscire dal ciclo una volta che la capacità massima giornaliera di produzione 
                # è stata raggiunta
                if(len(dizionarioProduzioneMassimaRaggiunta)==len(self.prodotti)):
                    minutiGiornalieriSuperati = True
        else:
            dizionarioParziale = self.getDizionarioProduzioneTotale()
        self.tempoLottoParziale = int(contatoreMinutiGiornalieri)
        return dizionarioParziale
    
    # Nome metodo: getDizionarioProduzioneTotale
    # Parametri in input: istanza attuale della classe lotto (oggetto)
    # Descrizione: metodo utilizzato per ottenere il dizionario composto da tutte le quantità di prodotti
    def getDizionarioProduzioneTotale(self):
        dizionarioLottoTotale = {}
        for i in self.prodotti:
            dizionarioLottoTotale[i.tipoDiProdotto] = int(i.quantita)
        return dizionarioLottoTotale
     
    # Nome metodo: __str__
    # Parametri in input: istanza attuale della classe Lotto (oggetto)
    # Descrizione: metodo utilizzato per mostrare a video le informazioni principali del Lotto
    def __str__(self):
        # inizializzazione variabile per controllare che il lotto abbia almeno un prodotto
        lottoProducibile = False
        stringaDiRitorno = "\n"

        #  verifica che ci sia almeno un prodotto
        for i in self.prodotti:
            if(i.quantita!=0):
                # se c'è, si procede con l'uscita dal ciclo e il censimento della fattibilità di produzione
                lottoProducibile = True
                break

        # se il lotto è producibile si prosegue con la creazione dei dizionari e la successiva stampa del resoconto
        if(lottoProducibile):

            dizionarioLottoTotale = self.getDizionarioProduzioneTotale()
            dizionarioLottoParziale = self.getDizionarioProduzioneMassimaGiornaliera()

            stringaDiRitorno = "Il tempo di produzione del lotto parziale composto da "+formattazioneStringaPerStampaValori(dizionarioLottoParziale)+" è di "+formattazioneStringaTempistiche(self.tempoLottoParziale)+"."
            
            stringaDiRitorno +="\n\nIl tempo di produzione necessario per creare l'intero lotto composto da "+formattazioneStringaPerStampaValori(dizionarioLottoTotale)+" è di "+formattazioneStringaTempistiche(self.tempoLottoTotale)+".\n"
        else:
            # se invece il lotto non è producibile si comunica all'utente l'impossibilità di creazione
            stringaDiRitorno = "Nel lotto non ci sono prodotti da creare."
    
        return stringaDiRitorno



    
