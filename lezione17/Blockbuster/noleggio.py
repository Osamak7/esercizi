from film import Film

class Noleggio:
    def __init__(self , film_list:list[Film]) -> None:
        self.film_list= film_list
        self.ranted_film :dict[str , list[Film]]={}
    
    def isAvaible(self , title):
        if title in self.film_list:
            print( f"Il film scelto è disponibile: {title}!")
            return True
        else:
            print(f"Il film scelto è disponibile: {title}!")
            return False

    def rentAMovie(self, film , clientID):
        if film in self.film_list:
            film_rimosso:Film= self.film_list.pop(film)
            self.ranted_film[clientID].append(film_rimosso)
            print( f"Il cliente {clientID} ha noleggiato {film}!")
        else:
            print(f"Non è possibile nolegiare il film {film}!")

    def giveBack(self,film, clientID, days):
        if film in self.ranted_film[clientID]:
            self.film_list.append(film)
            self.ranted_film[clientID].remove(film)



            