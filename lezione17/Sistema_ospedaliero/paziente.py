from persona import Persona

class Paziente(Persona):

    def __init__(self, first_name: str, last_name: str , __codice_identificativo:str) -> None:
        super().__init__(first_name, last_name)

        self.__codice_identificativo = __codice_identificativo
    
    def SetIdCode(self, idCode):
        self.__codice_identificativo= idCode
        
    def getIdCode(self):
        return self.__codice_identificativo
    
    def patientInfo(self):
        print(f"Paziente: {self.__first_name} {self.__last_name} \nID: {self.__codice_identificativo}")