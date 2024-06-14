class Persona:
    age:int=None
    def __init__(self , first_name:str , last_name:str ) -> None:
        self.first_name= first_name
        self.last_name= last_name
        self.age=Persona.age

    def setName(self, first_name):
        if type(first_name) == str:
            self.first_name=first_name
        else:
            self.first_name = None
            print("Il nome inserito non è una stringa!")
    
    def setLastName(self, last_name):
        if type(last_name) == str :
            self.last_name=last_name
        else:
            self.last_name= None
            print("Il cognome inserito non è una stringa!")
    
    def setAge(self, age):
        if  type(age) == int:
            self.age = age
        else: 
            self.age=None
            print("L'età deve essere un numero intero!")
        
    def getName(self):
        print(self.first_name)
    
    def getLastName(self):
        print(self.last_name)
    
    def Age(self):
        print(self.age)
    
    def greet(self):
        print(f"Ciao, sono {self.first_name} {self.last_name}! Ho {self.age} anni")


        