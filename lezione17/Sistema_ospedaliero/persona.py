class Persona:
    """Tale metodo, deve verificare che first_name, last_name siano stringhe; 
    in caso negativo, impostare a None l'attributo che non risulta essere una stringa,
      stampando un messaggio di errore, ad esempio, "Il nome inserito non è una stringa!". 
      Se first_name e last_name sono due stringhe, assegnare 0 
    all'attributo relativo all'età di una persona; se first_name e last_name non sono due stringhe, allora assegnare None all'età.
    """
    def __init__(self , first_name:str , last_name:str , age = None) -> None:
        self.__first_name= first_name
        self.__last_name= last_name
        self.__age= age

        if type(self.__first_name) != str:
            print("Il nome inserito non è una stringa!")
            self.__first_name= None

        if type(self.__last_name) != str:
            print("Il cognome inserito non è una stringa!")
            self.__last_name=None
        
        if type(self.__first_name) == str == type(self.__last_name):
            self.__age=0

    def setName(self, first_name):
        if type(first_name) == str:
            self.__first_name=first_name
        else:
            self.__first_name = None
            print("Il nome inserito non è una stringa!")
    
    def setLastName(self, last_name):
        if type(last_name) == str :
            self.__last_name=last_name
        else:
            self.__last_name= None
            print("Il cognome inserito non è una stringa!")
    
    def setAge(self, age):
        if  type(age) == int:
            self.__age = age
        else: 
            self.__age=None
            print("L'età deve essere un numero intero!")
        
    def getName(self):
        return self.__first_name
    
    def getLastName(self):
        return self.__last_name
    
    def getAge(self):
        return self.__age
    
    def greet(self):
        a : str =f"Ciao, sono {self.__first_name} {self.__last_name}! Ho {self.__age} anni"
        print(a)
        return a

        