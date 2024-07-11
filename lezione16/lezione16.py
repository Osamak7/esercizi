class Media:
    def __init__(self, title:str , reviews:list[int]) -> None:
        self.title=title
        self.reviews=reviews
        self.rate = None
        self.media= None

    def set_title(self , title:str):
        self.title = title

    def get_title(self):
        pass
    def aggiungiValutazione(self , voto:int):
        if voto in range(1,6):
            self.reviews.append(voto)
        else:
            return f"il voto non è valido"

    def getMedia(self):
        r:int=0
        val:str = ""
        for v in self.reviews:
            r += v
        result :float = r / len(self.reviews)

        if  result == 1:
            val = "Terribile"
        if result ==2 :
            val ="Brutto"
        if  result == 3:
            val = "Normale"
        if result ==4 :
            val ="Bello"
        if result == 5:
            val = "Grandioso"

        self.media = val
        return f" la media è {val}"
    
    def getRate(self):
        return f"il giudizio su questo film è : \"{self.rate}\""
    
    def Percentage(self , voto :int):
        percentuale : float= (voto* 5 )/100
        return f"la media in percentuale è :{ percentuale}"
    
    def recensione(self):
        return f"""titolo del film : {self.title} \n Voto Medio : {self.media} \n

                    Giudizio : {self.rate} \n
                    te"""
    





class Film(Media):
    def __init__(self, title: str, reviews: list[int]) -> None:
        super().__init__(title, reviews)
        self.title=title
        self.reviews=reviews
        self.rate:int = 0