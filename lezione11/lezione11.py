# Es 1
# Sistema di Prenotazione Cinema

class Film:
    def __init__(self , titolo_film : str  , durata_film :float ):
        self.titolo_film = titolo_film
        self.durata_film = durata_film
       
class Sala:

    def __init__( self, id:str , num_posti_tot :int , posti_prenotati :int) -> None:
        self.id = id
        
        self.num_posti_tot = num_posti_tot
        self.posti_prenotati = posti_prenotati
        self. posti_disponibili: int = num_posti_tot - posti_prenotati
        
        self.titolo_film : str =""
        self.durata : float = 0.00

    def add_film( self , film :Film):
        self.titolo_film = film.titolo_film
        self.durata = film.durata_film

    def prenota_posti(self, num_posti : int):
        self. posti_disponibili -= num_posti

class Cliente:
    def __init__(self , nome :str , cognome :str , codice : str) -> None: 
        self.nome= nome 
        self.cognome= cognome 
        self.codice=codice # il codice lo uso come esistenza del cliente poiche e presente nel codice a barre del biglietto o dell'abbonamento 
    


class Cinema:
    def __init__(self, nome:str) -> None:
        self.nome = nome
        self.lista_sale: list[Sala] = []
        self.lista_clienti : dict[ str , str ] = {}
        
        

    def add_sala(self, sala :Sala ):
        self.lista_sale.append(sala)
        print(f"la sala {sala.id} e stata aggiunta e trasmette {sala.titolo_film}")

    def add_cliente(self , cliente:Cliente):
        self.lista_clienti.update({cliente.codice: cliente.nome})
     


    def prenota_film(self, titolo_film : str , num_posti : int , codice:str):

        if codice in self.lista_clienti:
            
            for v in self.lista_sale:
                
                if titolo_film == v.titolo_film:
                    
                    if  (v.posti_disponibili - num_posti) > 0 :
                        v.prenota_posti(num_posti)
                        return f"Benvenuto {self.lista_clienti[codice]} posti prenotati: {num_posti}  posti ancora disponibili  : {v.posti_disponibili}"
                    
                    return f"ci disiace ma non ci sono {num_posti}  posti  i posti disponibili per questo film sono : {v.posti_disponibili}"
            else:
                ValueError("ci dispiace il film non e nel catalogo ")
        else:
            return f"non hai un biglietto o un abbonamento fanne uno poi ritorna grazie"

gestore= Cinema("osama")
sala1=Sala(id="1234567890" ,num_posti_tot =20, posti_prenotati =5)
film1=Film( titolo_film="Batman", durata_film=1.20 )
sala1.add_film(film1)
gestore.add_sala(sala1)

cliente1=Cliente(nome="Pinko" , cognome="Pallino" , codice="777")
gestore.add_cliente(cliente1)
print(gestore.prenota_film(titolo_film="Batman" ,num_posti=3 ,codice="777" ))
print(gestore.prenota_film(titolo_film="Batman" ,num_posti=3 ,codice="777" ))

print("*"*30)

# es2 
# Gestione di un magazzino

class Prodotto:
    def __init__(self, nome: str, quantita: int) :
        self.nome = nome
        self.quantita = quantita

class Magazino :
    def __init__(self , nome_magazziniere: str):
        self.nome_magazziniere = nome_magazziniere
        self.prodotti: dict[str , int]={}

    def aggiungi_prodotto(self, prodotto:Prodotto):
        self.prodotti.update({prodotto.nome : prodotto.quantita})
        return f"{prodotto.nome} e stato aggiunto al magazino disponibilita: {prodotto.quantita}"

    def cerca_prodotto(self , nome:str):
        if nome in self.prodotti:
            return f"{nome} e nel catalogo dei prodotti che trattiamo"
        else:   
            return f"{nome} non e tra i podotti che trattiamo"
        
    def verifica_disponibilita(self, nome:str):
        if nome in self.prodotti:
            return f"Di {nome} nel magazzino ce ne sono: {self.prodotti[nome]} "
        else:
            return f"{nome} non e tra i podotti che trattiamo"


prodotto1=Prodotto(nome="mela" , quantita=10)
magazziniere1= Magazino("Pippo")
print(magazziniere1.aggiungi_prodotto(prodotto1))
print(magazziniere1.verifica_disponibilita(nome="mela"))
print(magazziniere1.cerca_prodotto("mela"))