

class Film:
    def __init__(self,codice_identificativo:int , titolo:str) -> None:
        self.__codice_identificativo=codice_identificativo
        self.__titolo=titolo

    def setID(self, id):
        self.__codice_identificativo=id

    def setTitle(self, title):
        self.__titolo=title
    
    def getID(self):
        return self.__codice_identificativo

    def getTitle(self):
        return self.__titolo
    
    def isEqual(self, otherFilm ):
        if self.getID() == otherFilm.getID():
            return True
        else :
            return False

