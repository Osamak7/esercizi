
class Libro:
    def __init__(self , titolo:str , autore:str , stato_del_prestito:bool ) -> None:
        self.titolo=titolo
        self.autore=autore
        self.stato_del_prestito=stato_del_prestito

class Biblioteca:
    
    catalogo: list[Libro]= []
    libri_prestati: list[Libro]= []

    def add_book(self, libro:Libro):
        if libro.stato_del_prestito:
            self.catalogo.append(libro)
            return f"il libro \"{libro.titolo}\" aggiunto al catalogo"
        else:                      
            self.libri_prestati.append(libro)
            return f"il libro {libro.titolo} aggiunto hai libri prestati"
        
    def presta(self, titolo:str):
        i:int=0
        for l in self.catalogo:
            if l.titolo == titolo:
                self.libri_prestati.append( self.catalogo.pop(i))
                return f"il libro {titolo} e stato prestato con successo"
            i+=1
        for l in self.libri_prestati:
            if l.titolo== titolo:
                return f"Il libro {titolo} e gia stato prestato ci dispiace"
        
        return f"Il libro {titolo} non e al momento tra i libri in nostro possesso "
    
    def restituisci(self, titolo:str):
        i:int=0
        for l in self.libri_prestati:
            if l.titolo == titolo:
                self.catalogo.append(self.libri_prestati.pop(i))
                return f"il libro { titolo} e stato restituito con successo"
        
            i+=1
            
    def mostra_libri(self):
        for l in self.catalogo:
            print( f"libro : {l.titolo} \nautore : {l.autore}\n")
        
libro1= Libro(titolo="Pinko" , autore="Raffaello" , stato_del_prestito=True )
libro2= Libro(titolo="MMMM" , autore="Michele" , stato_del_prestito=True )
libro3= Libro(titolo="haha" , autore="Michele" , stato_del_prestito=True )


b = Biblioteca()
print(b.add_book(libro1))
print(b.add_book(libro2))
print(b.add_book(libro3))
print()
b.mostra_libri()
print(b.presta("Pinko"))
print()
b.mostra_libri()
print(b.restituisci("Pinko"))
b.mostra_libri()

