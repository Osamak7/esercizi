from persona import Persona

class Dottore(Persona):
    def __init__(self, first_name: str, last_name: str , specializzazione:str = None , parcella:float =None ) -> None:
        super().__init__(first_name, last_name)

        self.specializzazione = specializzazione
        self.parcella= parcella

    def setSpecializzazione(self, specializzazione):
        if type(specializzazione) == str:
            self.specializzazione=specializzazione
        else:
            print("La specializzazione inserita non è una stringa!")
    
    def setParcel(self,parcella):
        if type(parcella) == float:
            self.parcella = parcella
        else:
            print("La parcella inserita non è un float!")
        
    def getSpecialization(self):
        print(self.specializzazione)
    
    def getParcel(self):
        print(self.parcella)

    def isAValidDoctor(self):
        if self.age > 30 :
            print( f"Doctor {self.first_name} {self.last_name} is valid!")
        else:
            print(f"Doctor {self.first_name} {self.last_name} is not valid!")
    
    def doctorGreat(self):
        self.greet()
        print(f"Sono un medico {self.specializzazione}")

