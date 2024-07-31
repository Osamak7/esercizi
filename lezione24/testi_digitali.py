

class Documento:
    def __init__(self , testo:str) -> None:
        self.testo= testo    

    def getText(self):
        return self.testo

    def setText(self, testo_new:str):
        self.testo=testo_new
    
    def isInTest(self,parola:str):
        if parola in self.testo:
            return True
        else :
            return False
    
class Email(Documento):
    def __init__(self, testo: str , mittente:str , destinatario:str , titolo:str) -> None:
        super().__init__(testo)
        self.mittente=mittente
        self.destinatario = destinatario
        self.titolo =titolo
        

testo:str=Documento("ciaoo come va")
