
class Pagamento:
    def __init__(self) -> None:
        self.importo_pagamento: float = None

    def setPagamento(self,importo):
        self.importo_pagamento= importo

    def getPagamento(self):
        return f"Il tuo pagamento e di : {self.importo_pagamento:.2f}€"# :.2f  spiegazione (:) specificano che e una formattazione , (.2) il numero di elementi , (f) che e un numero float
    
    def dettagliPagamento(self):
        return f"Importo del pagamento: {self.importo_pagamento:.2f}€"


class PagamentoContanti(Pagamento):

    def dettagliPagamento(self):
        return f"Importo del pagamento in contanti: {self.importo_pagamento:.2f}€"
    
    def inPezziDa(self):
        
        dizionario_valute: dict[ int|float : int ]={500: 0 , 200: 0 , 100: 0 , 50: 0 , 20: 0 , 10: 0 , 5: 0 , 2: 0, 1: 0 , 0.50 : 0 , 0.20: 0 , 0.10: 0 , 0.05: 0 , 0.02: 0 , 0.01: 0 }

        conto:float=0.00
        while conto < self.importo_pagamento:

            for k in dizionario_valute:
                if conto + k <= self.importo_pagamento:
                    conto += k
                    dizionario_valute[k] += 1

        print(f"{self.importo_pagamento:.2f} da pagare in contanti con:")
        for k,v in dizionario_valute.items():
            if dizionario_valute[k] != 0 :
                print(f"{k:.2f}€ : {round(v,2)}")

class PagamentoCartaDiCredito(Pagamento):
    def __init__(self , nome:str , data_scadenza:str , numero_carta=int) -> None:
        self.nome=nome
        self.data_scadenza= data_scadenza
        self.numero_carta=numero_carta
    
    def dettagliPagamento(self):
        return (f"Pagamento di {self.importo_pagamento:.2f} effettuato con la carta di credito \n"
        f"Nome sulla carta: {self.nome}\n"
        f"Data di scadenza: {self.data_scadenza}\n"
        f"Numero della carta: {self.numero_carta}" 
        )

cliente1=PagamentoContanti()
cliente1.setPagamento(500.20)
print(cliente1.dettagliPagamento())
cliente1.inPezziDa()
print("*"*30)
cliente2=PagamentoCartaDiCredito("Luigi","19/07", 1234567890)
cliente2.setPagamento(1000.50)
print(cliente2.dettagliPagamento())