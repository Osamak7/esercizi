from typing import Any

class ContoBancario:
    total_account:int=0
    def __init__(self, nome :str , iban :int , saldo:float) -> None:
        self.nome=nome
        self.iban=iban 
        self.saldo=saldo

        ContoBancario.total_account+=1
    
    def deposito(self, importo :int):
        self.saldo += importo
        print(f"Deposito è di {importo} il tuo nuovo saldo è {self.saldo}")

    def prelievo(self, importo:int ):
        self.saldo-=importo 
        print(f"Hai prelevato {importo} il tuo nuovo saldo è di {self.saldo} ")

    @classmethod
    def get_total_account(cls):
        print(f"Account totali creati: {cls.total_account}")     

    @staticmethod
    def valida_account(iban:Any):
        if isinstance(iban, int) and len(str(iban))==  10: # is istance (iban , int ) contolla se iban e un intero e in caso lo sia restituisce True altrimenti False
            print("iban valido")
            return True
        else:
            print("Iban non valido")
            return False
            
account1= ContoBancario("Mimmo",1234567890,0)
account2= ContoBancario("Ruby",6789012345,1000)

account1.deposito(500)
account1.prelievo(200)

account2.deposito(200)
account2.prelievo(500)

ContoBancario.get_total_account()

ContoBancario.valida_account(1234567890)
ContoBancario.valida_account("123567890")

account3=ContoBancario("Luca",3456789012,1230)

ContoBancario.get_total_account()