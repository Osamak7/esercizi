
class Filiale:
    filiali_create:int=0

    def __init__(self , codice: str , indirizzo: str ) -> None:
        self.codice=codice
        self.indirizzo=indirizzo
       
        Filiale.filiali_create+=1

    @classmethod
    def totale_filiali_crate(cls):
        return f"numero filiali create : {cls.filiali_create}"
    
class Banca:
    def __init__(self, nome:str , simbolo:str) -> None:
        self.nome = nome
        self.simbolo: str = simbolo
        self.lista_filiali: list[Filiale] = []
        
    def numero_filiali(self):
        return len(self.lista_filiali)
    
    def aggiungi_filiale(self , filiale:Filiale):
        if self.simbolo in filiale.codice:
            self.lista_filiali.append(filiale)
        else:
            raise ValueError(f"la filiale appartiene ad un altra banca" )

unicredit = Banca(nome="Unicredit", simbolo= "UCG")
intesa = Banca(nome="Intesa San Paolo",simbolo="ISP")
filiale_unicredit1= Filiale(codice="UCG91",indirizzo="via sierra nevada , 60, Roma, Italia")
filiale_intesa1= Filiale(codice="ISP01",indirizzo="piazza barberini , Roma, Italia")

intesa.lista_filiali.append(filiale_intesa1)
unicredit.lista_filiali.append(filiale_unicredit1)


print(intesa.numero_filiali())
print(unicredit.numero_filiali())

print(Filiale.totale_filiali_crate())