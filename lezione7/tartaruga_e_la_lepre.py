
def posizione_tartaruga(indice):
    t=1
    if 1 <= indice <= 10 :
        pass
        # intero a caso, i, nell'intervallo 
    if 1 <= indice <= 5:
        t+=3
        #passo veloce
        pass     

    if 6 <= indice <= 7:
        if t - 6 >= 1:
            t-=6
        else :
            t=1
        
    if 8 <= indice <= 10:
        t+=1
        pass

def gara():
    pass

def Posizione_lepre(indice):
    if 1 <= indice <= 10 :
        # intero a caso, i, nell'intervallo 
        pass
    if 1 <= indice <= 5:
        #passo veloce
        pass     
    if 6 <= indice <= 7:
        # "scivolata"  
        pass

    if 8 <= indice <= 10:
        # "passo lento" 
        pass


def gara():
    percorso:list=["-"]*70
    tartaruga:str = 1
    lepre:str = 1
    indice:int=1
    print("\'BANG !!!!! AND THEY'RE OFF\ !!!!!'")
    while lepre < len(percorso) or tartaruga < len(percorso):

        Posizione_lepre(indice)
        posizione_tartaruga(indice)
        percorso.insert(indice)
        indice+=1
        
        

gara()