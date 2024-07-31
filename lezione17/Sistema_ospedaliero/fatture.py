from dottore import Dottore
from paziente import Paziente

class Fattura :
    def __init__(self , patient:list[Paziente], doctor : Dottore) -> None:
        self.__patient=patient
        self.__doctor = doctor
        if self.__doctor.isAValidDoctor() :
            self.__fatture= len(self.__patient)
        else: 
            self.__fatture:int=0
            self.__doctor.__age=None
            self.__doctor.__first_name=None
            self.__doctor.__last_name=None
            self.__doctor.__parcella=None
            print("Non è possibile creare la classe fattura poichè il dottore non è valido!")
        
    def getSalary(self):
        salario:float= (self.__doctor.getParcel() * len(self.__patient))
        salario = round(salario , 3)
        return salario
    
    def getFatture(self):
        self.__fatture= len(self.__patient)
        return self.__fatture
    
    def addPatient(self, newPatient:Paziente):
        self.__patient.append(newPatient)
        self.getFatture()
        self.getSalary()
        ris:str=f"Alla lista del Dottor {self.__doctor.getLastName()} è stato aggiunto il paziente {newPatient.getIdCode()}"
        print(ris)
        return ris
    
    def removePatient(self,idCode):
        for paziente in self.__patient :
            if paziente.getIdCode() == idCode:
                self.__patient.remove(paziente)
        self.getFatture()
        self.getSalary()
        ris:str=f"Alla lista del Dottor {self.__doctor.getLastName()} è stato rimosso il paziente {idCode}"
        print(ris)
        return ris


    