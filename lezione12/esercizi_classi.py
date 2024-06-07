#es 1
# es Sistema di Gestione Biblioteca
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

#es 2
# Catalogo Film 
class MovieCatalog:
    catalogo:dict[str, list[str]]={}
    

    def add_movie(self, director_name:str , movies: list[str]):
        if director_name not in self.catalogo:
            self.catalogo[director_name] = movies
        else:
            for movie in movies:
                if movie not in self.catalogo[director_name]:
                    self.catalogo[director_name].append(movie)
    
    def remove_movie(self , director_name:str, movie_name:str):

        if director_name in self.catalogo :
            for movie in self.catalogo[director_name]:
                if movie == movie_name:
                    self.catalogo[director_name].remove(movie_name)
                if  len( self.catalogo[director_name]) ==0:
                    del self.catalogo[director_name]
                    return f"il catalogo del regista {director_name} e stato eliminato perche vuoto"
            return f"il film \"{movie_name}\" non e presente nel catalogo quindi non puo essere eliminato"
        else:
            return f"il regista {director_name} non e presente nei nostri registri"
    
    def elenco_registi(self):
        registi= self.catalogo.keys()
        return registi
    def get_movie(self,director_name:str):
        return f"i film di {director_name} sono : {self.catalogo[director_name]}"
    
    def search_movie_by_film(self, title: str):
        risultati:list[tuple[str,str]] = []
        for regista, film in self.catalogo.items():
            if title in film:
                risultati.append((regista, title))
        if len(risultati)==0:
            return f"il film \" {title}\" non e presente nel catalogo"
        return risultati

                    
    

catalogo_film = MovieCatalog()

# Aggiunta di film al catalogo
catalogo_film.add_movie("Christopher Nolan", ["Inception", "Interstellar", "The Dark Knight"])
catalogo_film.add_movie("Quentin Tarantino", ["Pulp Fiction", "Kill Bill", "Django Unchained"])

# Ottenere un elenco di registi nel catalogo
registi = catalogo_film.elenco_registi()
print("Registi nel catalogo:", list(registi))

# Ottenere i film di un determinato regista
print(catalogo_film.get_movie("Christopher Nolan"))

# Rimozione di un film dal catalogo
print(catalogo_film.remove_movie("Christopher Nolan", "Interstellar"))

# Ottenere di nuovo i film di Christopher Nolan per verificare la rimozione
print(catalogo_film.get_movie("Christopher Nolan"))

# Cerco un film di Tarantino nel catalogo
print( catalogo_film.search_movie_by_film("Kill Bill"))
# cerco un film inesistente per vedere se mi ritorna che non e presente
print( catalogo_film.search_movie_by_film("pororo tomate"))
