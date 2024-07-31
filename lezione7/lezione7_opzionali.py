"""
1. Scrivi una funzione che prenda un dizionario e un valore, e ritorni la prima chiave che corrisponde a quel valore, o None se il valore non è presente."""

def es1(dizionario:dict , valore:int):
    keys= dizionario.keys() # assegno a keys tutte le chiavi del dizionario

    for k in keys: #controllo le chiavi per trvare una corrispondenzas
        if k == valore:
            return dizionario[k] 
    return None
print(es1({1:"x", 2:"y", 3:"z"} , 2))
print("*"*30)

"""2. Scrivi una funzione che inverte le chiavi e i valori in un dizionario. Se ci sono valori duplicati, scarta i duplicati."""
def invert_keys_value(dizionario:dict ): # disclamere do il nome solo alle funzioni che sembrano interessanti le altre le chiamo in base al numero dell'esercizio
    dizionario2:dict={}
    for k , v in dizionario.items():# faccio scorrere tutti i valori 
        dizionario2.update({v:k}) # aggiorno il nuovo dizionario con i valori invertiti del vecchio dizionario
    return dizionario2
print(invert_keys_value({1:"x", 2:"y", 3:"z"}))
print("*"*30)

"""3. Scrivi una funzione che riceve una lista di numeri, filtra i numeri pari, e restituisce una nuova lista con i numeri pari moltiplicati per un fattore dato."""
def es3(lista_numeri:list[int] , moltiplicatore:int):
    for n in lista_numeri[:]: #faccio scorrere una copia temporanea della lista
        lista_numeri.remove(n) #elimino tutti i valori della lista
        if n %2 == 0: 
            lista_numeri.insert(-1,n*moltiplicatore) # inserisco nella lista solo i valori pari moltiplicati dalla posizione -1 in modo da essere in ordine dal primo all'ultimo
    return lista_numeri 
print(es3([1,2,3,4,5,6,7,8,9],2))
print("*"*30)

"""4. Scrivi una funzione che determina se un numero è 'magico'. Un numero è considerato magico se è divisibile per 4 ma non per 6."""
def es4(numero_magico):
    if numero_magico % 4==0 and numero_magico % 6 !=0:
        return f"il numero {numero_magico} è un numero magico"
    return f"il numero {numero_magico} non è un numero magico"
print(es4(12))
print("*"*30)

"""5. Scrivi una funzione che accetti una lista di numeri e ritorni la somma dei numeri che sono divisibili sia per 2 che per 3."""
def es5(lista_num:list[int]):
    somma:int=0
    for num in lista_num:
        if num % 2==0 and num % 3==0:
            somma+= num
    return somma
print(es5([2,3,4,5,6,7,12,18]))
print("*"*30)

"""6. Scrivi una funzione che accetti un dizionario di prodotti con i prezzi e restituisca un nuovo dizionario con solo i prodotti che hanno un prezzo superiore a 20, scontati del 10%."""
def dict_product(dizionario:dict):
    new_dict:dict={}
    for k,v in dizionario.items():
        if v > 20:
            v-=v*10/100
            new_dict.update({k:v})
    return new_dict
print(dict_product({"mela":50,"pera":10,"cocomero":20,"ananas":35}))
print("*"*30)

"""7. Scrivi una funzione che prenda in input una lista di dizionari che rappresentano voti di studenti e aggrega i voti per studente in un nuovo dizionario."""
def value_for_student(dizionario_voti:dict[dict]):
    dizionario_voti2:dict[dict]={}
    
    for k , v in dizionario_voti.items():
        somma:int=0
        for  v1 in v.values():
            somma+=v1
        dizionario_voti2.update({k:{"somma voti":somma}})
    return dizionario_voti2
           

print(value_for_student( {"marco":{"matematica":7,"storia":10}, "fabio":{"matematica":10, "storia":10 } } ) )
print("*"*30)

"""8. Scrivi una funzione che elimini dalla lista dati certi elementi specificati in un dizionario. Il dizionario contiene elementi da rimuovere come chiavi e il numero di volte che devono essere rimossi come valori."""
def remuv_num_in_dict_for_list( dizionario: dict[int:int], lista_num: list[int]):
    for k,v in dizionario.items():
        for _ in range(v): # controllo i numeri che devo eliminare la chiave se è presente nella lista
            if k in lista_num[:]:#se la chiave e nella lista la elimino
                lista_num.remove(k)
            else:continue #se la chiave non è presente o in numero in cui deve essere eliminata persiste vado alla prossima chiave
    return lista_num
print(remuv_num_in_dict_for_list({1:2,2:1,3:2},[1,1,1,2,2,3]))
print("*"*30)

"""9. Scrivi una funzione che converta una lista di tuple (chiave, valore) in un dizionario. Se la chiave è già presente, aggiungi il valore alla lista di valori già associata alla chiave."""
def tuple_to_dict(tupla1:tuple,tupla2:tuple):
        dizionario:dict={}
        collection_keys:list=[]
        collezione_indici_copie:list=[]
        indice:int=0

        for chiave in tupla1:

            if chiave not in collection_keys:
                collection_keys.append(chiave)
                dizionario.update({chiave:list()})
                dizionario[chiave].append(tupla2[indice])

            else :
                collezione_indici_copie.append(indice)
                dizionario[chiave].append(tupla2[indice])

            indice+=1

        return dizionario


print(tuple_to_dict((1,2,3,4,1,2),("ciao","miao","bau","muu","zoo","floor")))
print("*"*30)

"""10. Scrivi una funzione che prende una lista di numeri e ritorna un dizionario che classifica i numeri in liste separate per numeri pari e dispari."""
def es10(num_list:list[int]):
    dizionario_pd:dict[str:list[int]]={"pari": [],"dispari":[]}
    for num in num_list:
        if num %2==0:
            dizionario_pd["pari"].append(num)
        else:
            dizionario_pd["dispari"].append(num)
    return dizionario_pd


print(es10((1,2,3,4,5,6,7,8,9)))
print("*"*30)

 
"""11. Scrivi una funzione che converte una temperatura da gradi Celsius a Fahrenheit e viceversa a seconda del parametro. Utilizza il concetto di parametri opzionali."""
def es11(gradi):
    pass

print("*"*30)

 
"""12. Scrivi una funzione che somma tutti i numeri interi di una lista che sono maggiori di un dato valore intero definito threshold."""
 
"""13. Scrivi una funzione che, data una lista, ritorni un dictionary che mappa ogni elemento alla sua frequenza nella lista."""
 
"""14. Scrivi una funzione che ritorna un dizionario che unisce due dizionari. Se una chiave è presente in entrambi, somma i loro valori nel nuovo dizionario."""
 
"""15. Scrivi una funzione che, dato un insieme e una lista di numeri interi da rimuovere, ritorni un nuovo insieme senza i numeri specificati nella lista."""
 
"""16. Scrivi una funzione che ritorna il valore massimo, minimo e la media di una lista di numeri interi."""
 
"""17. Scrivi una funzione che calcola la media di una lista di numeri e ritorna il valore arrotondato all'intero più vicino."""
 
"""18. Scrivi una funzione che rimuove tutti i duplicati da una lista, contenente sia numeri che lettere, mantenendo l'ordine originale degli elementi.
 
19. Scrivi una funzione che ruota gli elementi di una lista verso sinistra di un numero specificato k di posizioni. La rotazione verso sinistra significa che ciascun elemento della lista viene spostato a sinistra di una posizione e l'elemento iniziale viene spostato alla fine della lista. Per la rotazione utilizzare lo slicing e gestire il caso in cui il numero specificato di posizioni sia maggiore della lunghezza della lista.
 
20. Scrivi una funzione che accetti tre parametri: username, password e status di attivazione dell'account (attivo/non attivo). L'accesso è consentito solo se il nome utente è "admin", la password corrisponde a "12345" e l'account è attivo.
 
21. Scrivi una funzione che verifica se una combinazione di condizioni (A, B, e C) è soddisfatta per procedere con un'operazione. L'operazione può procedere solo se la condizione A è vera o se entrambe le condizioni B e C sono vere.
 
22. Scrivi una funzione che riceve un numero e stampa un conto alla rovescia da quel numero a zero.
 
23. Scrivi una funzione che, dato un numero intero, determina se è un "numero magico". Un numero magico è definito come un numero che contiene il numero 7.
 
24.  Scrivi una funzione che verifica se in una stringa le parentesi '(' e ')' sono bilanciate, cioè per ogni parentesi che apre c'è la corrispondente parentesi che chiude.
 
25. Scrivi una funzione che conta quante volte un elemento appare isolato in una lista di numeri interi. Un elemento è considerato isolato se non è affiancato da elementi uguali.
 
26. Scrivi una funzione chiamata create_contact() che accetta il nome e cognome, e-mail (facoltativo) e numero di telefono (facoltativo). La funzione dovrebbe restituire un dizionario con i dettagli del contatto.

ESEMPIO: create_contact("Mario Rossi", email="mario.rossi@gmail.com", telefono=69876543)

OUTPUT: {'profile': 'Mario Rossi', 'email': 'mario.rossi@gmail.com', 'telefono': 788787}

Scrivi una funzione chiamata update_contact() che accetta il dizionario creato, il nome e cognome del contatto da aggiornare, e il dettaglio facoltativo da aggiornare. Questa funzione dovrebbe aggiornare il dizionario del contatto.

ESEMPIO: update_contact(dict, "Mario Rossi", telefono=123456789)

OUTPUT: {'profile': 'Mario Rossi', 'email': 'mario.rossi@gmail.com', 'telefono': 123456789}

"""