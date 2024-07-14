

class Animale:
    def __init__(self , nome:str , specie:str , eta:int , verso:str) -> None:
        self.nome=nome
        self.specie=specie
        self.eta=eta
        self.verso=verso
    
    def fai_suono(self):
        return self.verso
    
class Cane(Animale):
    def __init__(self, nome: str, specie: str, eta: int, verso: str) -> None:
        super().__init__(nome, specie, eta, verso)


    def fai_suono(self):
        return super().fai_suono()
    
class Gatto(Animale):
    def __init__(self, nome: str, specie: str, eta: int, verso: str) -> None:
        super().__init__(nome, specie, eta, verso)

    def fai_suono(self):
        return super().fai_suono()
    
cane1 = Cane("pluto" , "cane" , 12 , "baubau")
print(cane1.fai_suono())
gatto1 =Gatto("silvestro" , "gatto " ,7 ,"miao" )
print(gatto1.fai_suono())