import random

def Posizione_tartaruga(avanzamento:int , energia : int):
 
    if 1 <= avanzamento <= 5:
        energia  =- 5
        avanzamento  = 3
        return avanzamento, energia

    if 6 <= avanzamento <= 7:
        energia = -10
        avanzamento = -6
        return avanzamento , energia
        
        
    if 8 <= avanzamento <= 10:
        energia= -3
        avanzamento = 1
        return avanzamento , energia 
    
    

def Posizione_lepre(avanzamento : int , energia:int):
    
    if 1 <= avanzamento <= 2:
        energia+=10
        avanzamento+=0

        return avanzamento , energia 

    elif 3 <= avanzamento <= 4:
        avanzamento+=9
        energia += -15
        return avanzamento , energia
            
    elif avanzamento <= 5:
        avanzamento += -12
        energia += -20
        return avanzamento , energia
    
    elif 6 <= avanzamento <=8:
        avanzamento+=1
        energia+=-5
        return avanzamento , energia
    
    elif 9<= avanzamento <= 10:
        avanzamento += -2
        energia+=8
        return avanzamento , energia
    
    
def meteo(clima:bool):
    if clima == False:
        clima=True
    else:
        clima= False

def gara():
    tartaruga:int = 1
    stamina_t:int = 100

    lepre:int = 1
    stamina_l:int = 100
    
    tic:int = 1
    percorso:dict = {}  
    clima:bool =  False

    for n in range(1,71):
        percorso[n]="_"

    print("\'BANG !!!!! AND THEY'RE OFF\ !!!!!'")
    while lepre < 70 and tartaruga < 70:
        avanzamento_l:int=0
        avanzamento_t:int=0
        
        energia_l:int=0
        energia_t:int=0

        if tic == 10:
            meteo(clima)
            tic = 0
        if clima == False:
            tartaruga-=1
            lepre-=2
        tic+=1


        pos_t = random.randint(1,10)
        pos_l = random.randint(1,10)
        
        avanzamento_l , energia_l = Posizione_lepre(pos_l , energia_l)
        avanzamento_t  , energia_t  = Posizione_tartaruga(pos_t, energia_t)

        stamina_l+= energia_l if stamina_l + energia_l > 0 else 0 , stamina_l 
        + 10
        stamina_t+= energia_t if stamina_t + energia_t > 0 else 0 , stamina_t + 10

        lepre += avanzamento_l if stamina_l  > 0 and lepre + avanzamento_l > 0 else 0
        tartaruga += avanzamento_t if stamina_t > 0 and tartaruga + avanzamento_t> 0 else 0
    
        if tartaruga <1:
            tartaruga=1
        if lepre<1:
            lepre=1

        if tartaruga > 70:
            tartaruga=70
        if lepre> 70:
            lepre=70

       
        if tartaruga == lepre:
            percorso[tartaruga]= "OUTCH"
        elif tartaruga != lepre:
            percorso[tartaruga]="T"
            percorso[lepre]= "H"
        
        print(tartaruga)
        print(lepre)
        #print(percorso)
        percorso[tartaruga]=""
        percorso[lepre]=""

    
    if tartaruga > lepre:
        print("TORTOISE WINS! || VAY!!!")
    elif lepre > tartaruga:
        print("HARE WINS || YUCH!!!")
    else:
        print("IT'S A TIE.")

        

gara()