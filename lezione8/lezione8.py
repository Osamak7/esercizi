class Animal:
    def __init__(self,name:str ,specie:str , eta:int ) :
        self.specie: str =specie
        self.eta :int =eta
        self.name=name
    def __str__(self) -> str:
         return f"nome ={self.name.capitalize()} \neta ={self.eta} \nspecie ={self.specie}"
     
    def verso(self):
        pass

class Cat(Animal):
    def __init__(self, name:str  ,specie: str, eta: int ) :
        super().__init__( name,specie, eta)
        
    def verso(self):
        return "Miao"
class Rabbit(Animal):
    def __init__(self, name:str ,specie: str, eta: int ) :
        super().__init__( name ,specie, eta)
        

class Persona(Animal):
    def __init__(self, eta: int , name:str ,cognome:str , cf:str ) :
        super().__init__(name ,"Homo sapiens", eta)
        self.cognome: str =cognome
        self.cf: str =cf

    def verso(self):
        return "ciao"

    def __str__(self) -> str:
        return f" nome ={self.name.capitalize()} \n cognome ={self.cognome.capitalize()} \n eta ={self.eta} \n specie ={self.specie}"
    
class Student(Persona):
    def __init__(self, specie: str, eta: int, name: str, cognome: str, cf: str , matricola:str) :
        super().__init__(name,specie, eta, cognome, cf)
        self.matricola: str = matricola

p=Persona(21,"lollo" , "Neri","bsdbfckied")
print(p)
print(p.verso())
g1=Cat("Garfield","gatto",12)
print("*"*20)
print(g1)
print(g1.verso())