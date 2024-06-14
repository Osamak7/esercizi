from dottore import Dottore
from paziente import Paziente

class Fattura :
    def __init__(self , patient:list[Paziente], doctor : Dottore) -> None:
        self.patient=patient
        self.doctor = doctor
        if self.doctor.isAValidDoctor() :
            self.fatture= len(self.patient)
        else: 
            self.fatture:int=0
            self.doctor.age=None
            self.doctor.first_name=None
            self.doctor.last_name=None
            self.doctor.parcella=None
            print("Non è possibile creare la classe fattura poichè il dottore non è valido!")
        
    def getSalary(self):
        salario:float= self.doctor.parcella * len(self.patient)
        print(salario)
    
    def getFatture(self):
        self.fatture= len(self.patient)
        return self.fatture
    
    def addPatient(self, newPatient:Paziente):
        self.patient.append(newPatient)
        self.getFatture()
        self.getSalary()
        print(f"Alla lista del Dottor {self.last_name} è stato aggiunto il paziente {newPatient.__codice_identificativo}")

    def removePatient(self,idCode):
        for paziente in self.patient :
            if paziente.__codice_identificativo == idCode:
                self.patient.remove(paziente)
        self.getFatture()
        self.getSalary()
        print(f"Alla lista del Dottor {self.doctor.last_name} è stato rimosso il paziente {idCode}")



    