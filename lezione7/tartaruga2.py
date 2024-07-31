import random
from typing import Any

def MovTartaruga(passi : int , stamina : int ):        # regolatore movimento tartaruga
    if   passi in range(1,6):
         passi= 3
         stamina += -5

    elif passi in range(6,8):
         passi = -6
         stamina += -10
        
    elif passi in range(8,11):
         passi = 1
         stamina += -3
    
    return passi , stamina


def MovLepre(passi : int  , stamina : int):            # regolatore movimento lepre
    
    if   passi in range(1,3) :
         passi = 0
         stamina += 10

    elif passi in range(3,5):
         passi = 9
         stamina += -15

    elif passi == 5 :
         passi = -12
         stamina += -20

    elif passi in range(6,9):
         passi = 1
         stamina += -5

    elif passi in range(9,11):
         passi = -2
         stamina += -8

    return passi , stamina


def Meteo(clima:bool):     # switch condizione climatica 
    return not clima

def Gara():
    percorso : dict [Any , Any] = {} 
    for n in range(1,71):
         percorso[n]="_"

    clima: bool = False
    tic : int = 0

    tartaruga : int = 1      # posizione  tartaruga
    t_stamina : int = 100    # energia  tartaruga
    t_passi : int = 0        # passi da aggiungere Tartaruga

    lepre : int = 1          # posizione lepre
    l_stamina : int = 100    # stamina lepre
    l_passi : int = 0        # passi da aggiungere Lepre
    

    while lepre < len(percorso) and tartaruga < len(percorso):  # ciclo finche uno dei due non raggiunge la lunghezza del percorso 

        if tic == 10 :     # switch ogni 10 tra pioggia e sole 
            clima= Meteo(clima)
            tic = 0

        if clima == True:  # se e true lo associo alla pioggia
            tartaruga = max(1, tartaruga - 1) # non potendo scendere sotto la posizione 1 confronto e scelgo il max tra 1 e il risultato della sotrazione
            lepre = max(1, lepre - 2)
            

        t_lancio :int = random.randint(1,10)    # simulo il lancio dei dadi e inserisco il valore nelle funzioni mov in base al risultato del dado si comportano in maniera diversa
        l_lancio :int = random.randint(1,10)    
        
        t_passi , t_stamina = MovTartaruga(t_lancio , t_stamina)
        l_passi , l_stamina = MovLepre(l_lancio , l_stamina)


        if t_stamina > 0 and tartaruga + t_passi > 0: #controllo se la tartaruga ha abbastanza energia per fare i passi e che facendoli non esca dal percorso
            tartaruga += t_passi
        else: # altrimenti non eseguengo passi aquisisce stamina
            t_stamina += 10

      
        if l_stamina > 0 and lepre + l_passi > 0 :     # eseguo lo stesso controllo fatto sulla tartaruga 
            lepre += l_passi
        else :
            l_stamina += 10
            print(" lepre entrataaaaaaaaaaaaaaaaaaaaa")
        
        if t_stamina > 100: # eseguo dei controlli sulla stamina se sono andati in eccesso li ri bilancio per la prossima iterazione anche perche se sono in eccesso posso fare tutte le mosse 
            t_stamina =100
        if l_stamina > 100:
            l_stamina = 100

        if tartaruga <1:    # faccio in modo che la tartaruga non vadano sotto la posizione 1 poiche l'inizio e da li 
            tartaruga=1
        if lepre<1:         
            lepre=1

        if tartaruga > 70:  # per lo stesso principio non possono superare la lunghezza della lista
            tartaruga=70
        if lepre> 70:
            lepre=70

       
        if tartaruga == lepre:          # se sono nella stessa posizione printo "OUTCH" per indicare che la tartaruga morde la lepre
            percorso[tartaruga]= "OUTCH"
        elif tartaruga != lepre:        # altrimenti se sono in posizioni diverse li assegno alle loro posizioni 
            percorso[tartaruga]="T"
            percorso[lepre]= "H"
        print(f"lepre stamina , passi , posizione {l_stamina , l_passi , lepre } \n tartaruga stamina , passi , posizione {t_stamina , t_passi , tartaruga } \n")
        # print(f"{percorso}\n") # stampo il percorso con la posizione attuale e successivamente resetto come erano all'inizio
        # percorso[tartaruga] = "_"
        # percorso[lepre] = "_"
        tic +=1
        
    print(percorso)

Gara() 