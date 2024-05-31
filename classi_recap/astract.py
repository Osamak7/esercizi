
from abc import ABC , abstractmethod

class AbcAnimal(ABC):
    @abstractmethod
    def verso(self):
        pass
    def movimento(self , t:int):
        pass

class Cane(AbcAnimal):
    def __init__(self, nome:str) -> None:
        super().__init__()

        self.nome = nome
        self.velocita : float = 100.0  #m/s
    def verso(self):
        return print("BAU !!!")
    
    def movimento( self , t:int):
        print( self.velocita * t)


class Gatto(AbcAnimal):
    def __init__(self , nome:str) -> None:
        super().__init__()
        self.nome=nome
        self.velocita: float = 100.0 #m/s
    
    def verso(self):
        return print("MIAO !!!")
    
    def movimento( self , t:int):
        print( self.velocita * t)


cane1=Cane("Pluto")
cane1.verso()
cane1.movimento(10)
gatto1=Gatto("Silvestro")
gatto1.verso()
gatto1.movimento(t=20)
