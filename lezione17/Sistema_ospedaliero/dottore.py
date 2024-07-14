from persona import Persona

class Dottore(Persona):
    def __init__(self, first_name: str, last_name: str ,  specializzazione:str = None , parcella:float =None ) -> None:
        super().__init__(first_name, last_name)

        self.__specializzazione = specializzazione
        self.__parcella= parcella
        

        if type(self.__specializzazione) != str:
            self.__specializzazione=None
            print("La specializzazione inserita non è una stringa!")

        if type(self.__parcella)!= float:
            self.__parcella=None
            print("La parcella inserita non è un float!")

    def setSpecializzazione(self, specializzazione):
        if type(specializzazione) == str:
            self.__specializzazione=specializzazione
        else:
            print("La specializzazione inserita non è una stringa!")
    
    def setParcel(self,parcella):
        if type(parcella) == float:
            self.__parcella = parcella
        else:
            print("La parcella inserita non è un float!")
        
    def getSpecialization(self):
        return self.__specializzazione
    
    def getParcel(self):
        return self.__parcella

    def isAValidDoctor(self):
        a:str=""
        if self.getAge() > 30 :
            a=f"Doctor {self.getName()} {self.getLastName()} is valid!"

        elif  self.__age<=30:
            a= f"Doctor {self.getName()} {self.getLastName()} is not valid!"
        
        print(a)
        return a # metto il return per testare la funzione perche se nel test richiamo get_name , get_lastname non e come testare questa funzione ma le altre 
    
    
    def doctorGreat(self):
        a=self.greet()
        a+=f". Sono un medico {self.__specializzazione}"
        print(a)
        return a
