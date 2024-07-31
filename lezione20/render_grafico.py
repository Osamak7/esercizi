from abc import ABC,abstractmethod

class Forma(ABC):
    def __init__(self, nome:str) -> None:
        self.nome=nome

    @abstractmethod
    def getArea(self):
        pass

    @abstractmethod
    def render(self):
        pass

class Quadrato(Forma):
    def __init__(self, nome , lato:float) -> None:
        super().__init__("cerchio")
        self.lato=lato

    def getArea(self):
        area :float = self.lato**2
        return f"l'area del quadrato è di {area}"
    
    def render(self):
        print("*"*int(self.lato))
        
quad1=Quadrato("Quadrato",5.5)
quad1.render()
        