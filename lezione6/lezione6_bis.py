class Person :
    def __init__(self , 
                 nome:str , 
                 cognome:str , 
                 data_di_nascita:str , 
                 genere:str , 
                 codice_fiscale:str ) -> None:
        
        self.nome= nome 
        self.cognome=cognome
        self.data_di_nascita=data_di_nascita
        self.genere=genere
        self.codice_fiscale :str =codice_fiscale

    def calcola_eta(self) -> int:
        return 10
    
    def __eq__(self, value: object) -> bool:
        return value.codice_fiscale == self.codice_fiscale




class Dipendente(Person):
    def __init__(self, nome: str, 
                 cognome: str, 
                 data_di_nascita: str, 
                 genere: str ,
                 codice_fiscale:str , 
                 ore_lavorate:int=500) -> None:
        super().__init__(nome, cognome, data_di_nascita, genere,codice_fiscale)

        self.ore_lavorate:int= ore_lavorate

    
    def calcola_stipendio(self)->float:
        return 500.00

class Professore(Dipendente):
    def __init__(self, nome: str, cognome: str, data_di_nascita: str, genere: str, ore_lavorate: int , codice_fiscale:str , materia_insegnata:str , ore_di_lezione : int =1000) -> None:
        super().__init__(nome, cognome, data_di_nascita, genere,codice_fiscale, ore_lavorate ,)

        self.materia_insegnata=materia_insegnata
        self.ore_di_lezione=ore_di_lezione




        
dipendente1:Dipendente=Dipendente("omar","mamadu","21/03/1996","M","")

persona1:str=Person("osama",
                    "hliwa",
                    "19/09/2001" , 
                    "M",
                    "lknfvnwerlnflknwe")

print(persona1.calcola_eta())
print(dipendente1.ore_lavorate)

professore_1:Professore=Professore(nome="lola",
                                   cognome="l",
                                   data_di_nascita="17/04/1993",
                                   genere="M",
                                   codice_fiscale="jbejbjenfdjn",
                                   ore_lavorate=77,
                                   materia_insegnata="Python"
                                   )
print(professore_1.materia_insegnata)