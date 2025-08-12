import random

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
    return int(random.uniform(1.0, 60.0))


# Nome classe: Prodotto
# Descrizione: classe genitore utilizzata per definire dei calcoli base utilizzabili da tutti i prodotti e mostrare la
# scheda del prodotto 
class Prodotto:
    # costante utilizzata per calcolare il numero di minuti in un giorno
    __numeroTotaleMinutiInUnGiorno = 60*24

    
    # Nome metodo: costruttore della classe Prodotto
    # Parametri in input: istanza attuale della classe prodotto (oggetto), numero di prodotti da creare (int), il tempo di produzione della singola unità del prodotto (int), 
    # la complessità del tipo di prodotto (int) e il tipo di prodotto da creare (str)
    # Descrizione: costruttore della classe Prodotto, utilizzato per incapsulare i dati che saranno poi utilizzati per calcolare il tempo
    # di produzione del lotto 
    def __init__(self,quantita,tempoDiProduzionePerSingolaUnita,complessitaDiProduzioneDelProdotto,tipoDiProdotto):
        self.quantita = quantita
        self.tempoDiProduzionePerSingolaUnita = tempoDiProduzionePerSingolaUnita*complessitaDiProduzioneDelProdotto
        self.complessitaDiProduzioneDelProdotto = complessitaDiProduzioneDelProdotto
        self.__tipoDiProdotto = tipoDiProdotto

    # Nome metodo: getCapacitaMassimaGiornalieraUnita
    # Parametri in input: istanza attuale della classe prodotto (oggetto)
    # Descrizione: metodo utilizzato per ottenere il numero massimo di unità producibili in un giorno.             
    def getCapacitaMassimaGiornalieraUnita(self):
        return self.__numeroTotaleMinutiInUnGiorno//self.tempoDiProduzionePerSingolaUnita

    # Nome metodo: getTempodiProduzioneTotale
    # Parametri in input: istanza attuale della classe prodotto (oggetto)
    # Descrizione: metodo utilizzato per ottenere il tempo di produzione di tutti i prodotti del singolo tipo  
    def getTempodiProduzioneTotale(self):
        return self.tempoDiProduzionePerSingolaUnita*self.quantita
    
    # Nome metodo: __str__
    # Parametri in input: istanza attuale della classe prodotto (oggetto)
    # Descrizione: metodo utilizzato per mostrare a video la scheda del prodotto     
    def __str__(self):
        return "*************************\nTipo di prodotto: "+ str(self.__tipoDiProdotto)+"\nQuantità in produzione: "+str(int(self.quantita))+"\nComplessità di creazione del tipo di prodotto: "+str(self.complessitaDiProduzioneDelProdotto)+"\nTempo di produzione per singola unità: "+str(self.tempoDiProduzionePerSingolaUnita)+" minuti\nCapacità massima giornaliera di produzione della singola unità: "+str(self.getCapacitaMassimaGiornalieraUnita())+" unità/giorno\n*************************"

# Nome classe: Smartphone
# Descrizione: classe prodotto specifico utilizzata per definire la scheda del prodotto 
class Smartphone(Prodotto):
    tipoDiProdotto = "Smartphone"
    __tempoDiProduzionePerSingolaUnita = tempoDiProduzioneOrario()
    __complessitaDiProduzioneDelProdotto = definisciComplessitaProdotto()
    # Nome metodo: costruttore della classe Smartphone
    # Parametri in input: istanza attuale della classe prodotto (oggetto), numero di prodotti da creare (int), il tempo di produzione della singola unità del prodotto (int), 
    # la complessità del tipo di prodotto (int) e il tipo di prodotto da creare (str)
    # Descrizione: costruttore della classe Smartphone, usato per passare le caratteristiche del tipo di prodotto alla classe genitrice
    # di produzione del lotto 
    def __init__(self, quantita):
        super().__init__(quantita,self.__tempoDiProduzionePerSingolaUnita,self.__complessitaDiProduzioneDelProdotto, self.tipoDiProdotto)
    
# Nome classe: Conchiglia
# Descrizione: classe prodotto specifico utilizzata per definire la scheda del prodotto    
class Conchiglia(Prodotto):
    tipoDiProdotto = "Telefono a conchiglia"
    __tempoDiProduzionePerSingolaUnita = tempoDiProduzioneOrario()
    __complessitaDiProduzioneDelProdotto = definisciComplessitaProdotto()

    # Nome metodo: costruttore della classe Conchiglia
    # Parametri in input: istanza attuale della classe prodotto (oggetto), numero di prodotti da creare (int), il tempo di produzione della singola unità del prodotto (int), 
    # la complessità del tipo di prodotto (int) e il tipo di prodotto da creare (str)
    # Descrizione: costruttore della classe Conchiglia, usato per passare le caratteristiche del tipo di prodotto alla classe genitrice
    # di produzione del lotto
    def __init__(self, quantita):
        super().__init__(quantita,self.__tempoDiProduzionePerSingolaUnita,self.__complessitaDiProduzioneDelProdotto, self.tipoDiProdotto)
    
# Nome classe: Fisso
# Descrizione: classe prodotto specifico utilizzata per definire la scheda del prodotto        
class Fisso(Prodotto):
    tipoDiProdotto = "Telefono fisso"
    __tempoDiProduzionePerSingolaUnita = tempoDiProduzioneOrario()
    __complessitaDiProduzioneDelProdotto = definisciComplessitaProdotto()

    # Nome metodo: costruttore della classe Fisso
    # Parametri in input: istanza attuale della classe prodotto (oggetto), numero di prodotti da creare (int), il tempo di produzione della singola unità del prodotto (int), 
    # la complessità del tipo di prodotto (int) e il tipo di prodotto da creare (str)
    # Descrizione: costruttore della classe Fisso, usato per passare le caratteristiche del tipo di prodotto alla classe genitrice
    # di produzione del lotto
    def __init__(self, quantita):
        super().__init__(quantita,self.__tempoDiProduzionePerSingolaUnita,self.__complessitaDiProduzioneDelProdotto, self.tipoDiProdotto)

# Nome classe: Lotto
# Descrizione: classe utilizzata per definire le caratteristiche del lotto di produzione            
class Lotto:
    tempoLottoParziale = 0
    tempoLottoTotale = 0
    NUMERO_MINUTI_GIORNALIERO = 1440

    # Nome metodo: costruttore della classe Lotto
    # Parametri in input: istanza attuale della classe lotto (oggetto), elenco di prodotti (lista)
    # Descrizione: costruttore della classe Lotto utilizzato per mostrare il resoconto dei prodotti del lotto
    # e calcolare il tempo totale di produzione
    def __init__(self, prodotti):
        for i in prodotti:
            print(i)
        self.prodotti = prodotti
        self.calcolaTempoTotaleLotto()


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
        
    # Nome metodo: formattazioneStringaPerStampaValori
    # Parametri in input: istanza attuale della classe lotto (oggetto), dizionario contenente l'elenco dei tipi di prodotti
    # con l'annessa quantità di ogni singolo prodotto
    # Descrizione: metodo utilizzato per formattare meglio l'elenco dei prodotti e rendere la stringa finale più leggibile
    def formattazioneStringaPerStampaValori(self,dizionarioQuantita):
        stringaFinale = ""
        # il dizionario viene iterato per concatenare il tipo di prodotto, la sua quantità e eventuali stringhe aggiuntive 
        # (tra cui la virgola)
        for i in dizionarioQuantita.keys():
            stringaFinale += str(dizionarioQuantita[i])+" unità del prodotto \""+ str(i)+"\","
        # la stringaFinale così composta viene decurtata della virgola finale 
        stringaFinale = stringaFinale[:-1]

        # la stringa finale subisce un'ulteriore lavorazione per ottenere un elenco di sotto-stringhe 
        elementi = stringaFinale.split(',')
        if len(elementi) > 1:
            # se la stringa ha più di due valori vuol dire che è possibile inserire la "e" al posto della virgola per una migliore lettura
            ultimo_elemento = elementi.pop()
            stringaFinale = ", ".join(elementi) + " e " + ultimo_elemento
        else:
            stringaFinale = stringaFinale
        return stringaFinale

    # Nome metodo: getDizionarioProduzioneMassimaGiornaliera
    # Parametri in input: istanza attuale della classe lotto (oggetto)
    # Descrizione: metodo per ottenere un dizionario di prodotti producibili in un giorno 
    def getDizionarioProduzioneMassimaGiornaliera(self):
        dizionarioParziale = {}
        dizionarioProduzioneMassimaRaggiunta = {}
        contatoreMinutiGiornalieri = 0
        minutiGiornalieriSuperati = False
        # l'elenco dei prodotti viene iterato per sommare il tempo di produzione di tutti i prodotti
        for i in self.prodotti:
            contatoreMinutiGiornalieri += i.getTempodiProduzioneTotale()

        # se la produzione è fattibile in un giorno posso restituire l'intero lotto 
        if(contatoreMinutiGiornalieri>self.NUMERO_MINUTI_GIORNALIERO):
            contatoreMinutiGiornalieri = 0
            # se la produzione totale non è fattibile in un giorno, cerco di ottenere un dizionario che contiene
            # più prodotti possibili di ogni tipo
            while contatoreMinutiGiornalieri<=self.NUMERO_MINUTI_GIORNALIERO and (not minutiGiornalieriSuperati):

                for i in self.prodotti:

                    # il tipo di prodotto corrente nel dizionarioParziale viene inizializzato a 0 se assente,
                    # altrimenti prende il valore corrente
                    dizionarioParziale[i.tipoDiProdotto] = dizionarioParziale[i.tipoDiProdotto] if i.tipoDiProdotto in dizionarioParziale else 0
                    # il prodotto viene inserito nel dizionario se non tutte le quantita dello stesso sono state aggiunte al dizionario parziale e 
                    # se il tempo di produzione del singolo prodotto non eccede il tempo giornaliero di produzione 
                    if ((dizionarioParziale[i.tipoDiProdotto]<i.quantita) and (not (i.tipoDiProdotto in dizionarioProduzioneMassimaRaggiunta))):
                        # il prodotto corrente viene inserito nel dizionario di produzione massima raggiunta per impedirne un'ulteriore produzione
                        if((contatoreMinutiGiornalieri+i.tempoDiProduzionePerSingolaUnita)>self.NUMERO_MINUTI_GIORNALIERO):
                            dizionarioProduzioneMassimaRaggiunta[i.tipoDiProdotto]=True
                        else:
                            # se il prodotto può essere aggiunto in quanto il tempo di produzione attuale non supera le 24h allora il 
                            # dizionarioParziale viene aggiornato con la nuova quantità
                            contatoreMinutiGiornalieri += i.tempoDiProduzionePerSingolaUnita
                            dizionarioParziale[i.tipoDiProdotto]+=1
                    else:
                        dizionarioProduzioneMassimaRaggiunta[i.tipoDiProdotto]=True
                # il seguente controllo viene utilizzato per uscire dal ciclo una volta che la capacità massima giornaliera di produzione 
                # è stata raggiunta
                if(len(dizionarioProduzioneMassimaRaggiunta)==len(self.prodotti)):
                    minutiGiornalieriSuperati = True

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

    # Nome metodo: calcoloTempoTotale
    # Parametri in input: istanza attuale della classe lotto (oggetto), tempoTotale in minuti
    # Descrizione: metodo utilizzato per calcolare il numero di giorni, il numero di ore e il numero di minuti usando il tempo totale in minuti
    # preso in input
    def calcoloTempoTotale(self, tempoTotale):
        numeroGiorni = tempoTotale//1440
        numeroOre = tempoTotale%1440//60
        numeroMinuti = tempoTotale%60
        return numeroGiorni, numeroOre, numeroMinuti
     
    # Nome metodo: __str__
    # Parametri in input: istanza attuale della classe Lotto (oggetto)
    # Descrizione: metodo utilizzato per mostrare a video le informazioni principali del Lotto
    def __str__(self):
        # dizionarioLottoTotale 
        dizionarioLottoTotale = self.getDizionarioProduzioneTotale()
        dizionarioLottoParziale = self.getDizionarioProduzioneMassimaGiornaliera()

        stringaDiRitorno = "\nNumero massimo di unità del lotto producibili in un giorno:\n"
        dizionarioLottoParziale = dizionarioLottoParziale if len(dizionarioLottoParziale) > 0 else dizionarioLottoTotale

        for i in dizionarioLottoParziale.keys():
            stringaDiRitorno += "\t- "+str(int(dizionarioLottoParziale[i]))+" unità del prodotto \""+str(i)+"\"\n"

        numeroGiorni, numeroOre, numeroMinuti = self.calcoloTempoTotale(self.tempoLottoParziale)
        stringaDiRitorno += "\nIl tempo di produzione del lotto giornaliero composto da "+self.formattazioneStringaPerStampaValori(dizionarioLottoParziale)+" è di "+(str(numeroGiorni)+(" giorno, " if numeroGiorni ==1 else " giorni, ") if numeroGiorni !=0 else "")+str(numeroOre)+(" ora e " if numeroOre ==1 else " ore e ")+str(numeroMinuti)+ (" minuto" if numeroMinuti ==1 else " minuti")+"."
        
        numeroGiorni, numeroOre, numeroMinuti = self.calcoloTempoTotale(self.tempoLottoTotale)
        stringaDiRitorno +="\n\nIl tempo di produzione necessario per creare l'intero lotto composto da "+self.formattazioneStringaPerStampaValori(dizionarioLottoTotale)+" è di "+(str(numeroGiorni)+(" giorno, " if numeroGiorni ==1 else " giorni, ") if numeroGiorni !=0 else "")+str(numeroOre)+(" ora e" if numeroOre ==1 else " ore e ")+str(numeroMinuti)+ (" minuto" if numeroMinuti ==1 else " minuti")+".\n"

    
        return stringaDiRitorno



    
