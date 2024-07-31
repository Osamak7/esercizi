import unittest
from persona import Persona
from dottore import Dottore
from paziente import Paziente 
from fatture import Fattura

class TestPersona(unittest.TestCase):
    pass
    def setUp(self) -> None:
        self.persona=Persona(first_name="Marco" , last_name="Rossi")
    # scrivo cosi self.persona._Persona__first_name perche essendo variabili private si richiamano scrivendo _Persona__nome

    def test_creazione_persona(self):
        self.assertEqual(self.persona.getName(),"Marco" , "il nome non e impostato correttamente")
        self.assertEqual(self.persona.getLastName(), "Rossi" , "il cognome non e impostato correttamente")
        self.assertEqual(self.persona.getAge() , 0 , "l'eta non e impostata correttamente")

    def test_setName(self):
        self.persona.setName("giorgio")
        self.assertEqual(self.persona.getName(), "giorgio" , "nome non corretto")
        
    def test_setLastName(self):
        self.persona.setLastName("Neri")
        self.assertEqual(self.persona.getLastName(), "Neri","il cognome non e cambiato")

    def test_setAge(self):
        self.persona.setAge(23)
        self.assertEqual(self.persona.getAge(),23 , "l'eta non e corretta")

    def test_greet(self):
        self.persona.setName("Giorgio")
        self.persona.setLastName("Neri")
        self.persona.setAge(23)
        self.assertEqual(f"Ciao, sono {self.persona.getName()} {self.persona.getLastName()}! Ho {self.persona.getAge()} anni" , 
                         f"Ciao, sono Giorgio Neri! Ho 23 anni", "stampa errata")



class TestDottore(unittest.TestCase):
    def setUp(self) -> None:
        self.dottore=Dottore(first_name="Mario", last_name="Milan",
                             specializzazione="Pediatra", parcella=21.20)
    
    def test_setUp(self):
        self.assertEqual(self.dottore.getName(), "Mario" , "il nome non e corretto")
        self.assertEqual(self.dottore.getLastName(),"Milan","il cognome non e corretto")
        self.assertEqual(self.dottore.getAge(),0, "l'eta non coincide")
        self.assertEqual(self.dottore.getParcel(), 21.20 , "la parcella non coincide")
        self.assertEqual(self.dottore.getSpecialization() , "Pediatra" , "la specializzazione non coincide")

    def test_setSpecializzazione(self):
        self.dottore.setSpecializzazione("Chirurgo")
        self.assertEqual(self.dottore.getSpecialization(),"Chirurgo", "specializzzione sbagliata")

    def test_setParcel(self):
        self.dottore.setParcel(30.10)
        self.assertEqual(self.dottore.getParcel() , 30.10 , "set Parcel sbagliato") 

    def test_isAvoidDoctor(self):
        self.dottore.setName("Pinko")
        self.dottore.setLastName("Pallino")
        self.dottore.setAge(45) #testato su diverse eta 
        self.assertEqual(self.dottore.isAValidDoctor(), 
                         f"Doctor Pinko Pallino is valid!" , "is avoid e sbagliato")
      
    def test_doctorGreat(self):
        self.assertEqual(self.dottore.doctorGreat(),
                        f"Ciao, sono Mario Milan! Ho 0 anni. Sono un medico Pediatra",
                        "test doctor great sbagliato")

class TestPaziente(unittest.TestCase):
    pass
    def setUp(self) -> None:
        self.paziente=Paziente("Paolo","Rossi","123456789")
        
    def test_setUp(self):
        self.assertEqual(self.paziente.getName(),"Paolo","nome errato")
        self.assertEqual(self.paziente.getLastName(),"Rossi","cognome errato")
        self.assertEqual(self.paziente.getIdCode(),"123456789","codice errato")
        self.assertEqual(self.paziente.getAge(),0,"eta errata")

    def test_setIdCode(self):
        self.paziente.SetIdCode("987654321")
        self.assertEqual(self.paziente.getIdCode(),"987654321","setId errato")

    def test_getIdCode(self):
        self.assertEqual(self.paziente.getIdCode(),"123456789","getId errato")

    def test_patientInfo(self):
        self.assertEqual(f"Paziente: {self.paziente.getName()} {self.paziente.getLastName()} \nID: {self.paziente.getIdCode()}",
                         f"Paziente: Paolo Rossi \nID: 123456789", "patientInfo errato")

class TestFattura(unittest.TestCase):
    def setUp(self) -> None:
        
        persona1=Paziente("Mario","Rossi","12345")
        persona2=Paziente("Giovanni","Bianchi","987654321")
        persona3=Paziente("Lorenzo","Neri","123456789")
        dottore=Dottore("Luigi","Ranieri","Chirurgo",40.10)
        dottore.setAge(45)
        self.fattura=Fattura(patient = [persona1 ,persona2 , persona3] , doctor = dottore)

    def test_setUp(self):
        self.assertEqual(self.fattura.getFatture(), 3, "setUp errore")
      
    def test_getSalary(self):
        self.assertEqual(self.fattura.getSalary() , 120.30, "getSalari errore")

    def test_getFatture(self):
        self.assertEqual(self.fattura.getFatture(), 3, "getFatture errore")
    
    def test_addPatient(self):
        paziente4= Paziente("Pippo","Knor","12345")
        self.assertEqual(self.fattura.addPatient(paziente4),
                         f"Alla lista del Dottor {self.fattura._Fattura__doctor.getLastName()} è stato aggiunto il paziente {paziente4.getIdCode()}")
        
    def test_removePatient(self):
        self.assertEqual( self.fattura.removePatient("12345") , 
                         f"Alla lista del Dottor Ranieri è stato rimosso il paziente 12345" , "removePatient errore")
"""
Test della Classe Fattura
- Creare una classe di test chiamata TestFattura che eredita da unittest.TestCase.
- Implementare il metodo setUp per inizializzare un oggetto Fattura con una lista di pazienti e un dottore valido.
- Scrivere test per verificare:
  - L'inizializzazione corretta della classe Fattura.
  - Il calcolo corretto del salario e del numero di fatture.
  - L'aggiunta e la rimozione di pazienti dalla lista."""





if __name__ == "__main__":
    unittest.main()