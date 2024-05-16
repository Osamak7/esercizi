class Fence:
    def __init__(self, area: float, temperature: int, habitat: str):
        self.area = area
        self.temperature = temperature
        self.habitat = habitat
        self.animals :list = []  
        self.lista_habitat:list=[]
        self.area=area
        self.area_totale=area
class Animal:
    def __init__(self, name: str, species: str, age: int, height: float, width: float, preferred_habitat: str):
        self.name = name
        self.species = species
        self.age = age
        self.height = height
        self.width = width
        self.preferred_habitat = preferred_habitat
        self.health = round(100 * (1 / age), 3)
        self.area = round((self.height * self.width), 3)
        self.fence: Fence = None

    def __str__(self) -> str:  # creo una funzione per stampare le caratteristiche
         return f"Animal (name={self.name} , species={self.species} , age={self.age}"




class Zookeeper:
    def __init__(self, name: str, surname: str, id: str):
        self.name = name
        self.surname = surname
        self.id = id
        

    def add_animal(self, animal: Animal, fence: Fence): #funzione che aggiunge un animale  in una gabbia 
        if animal.preferred_habitat == fence.habitat and fence.area - animal.area >= 0: #controllo se l'abitat preferito dell'animale e uguale all'abitat fornito  e se ce spazio sufficente per inserire l'animale
            fence.animals.append(animal)
            fence.area -= animal.area
            animal.fence=fence

    def remove_animal(self ,animal: Animal, fence: Fence):# rimuovo l'animale dall'abitat se e presente all'interno
         
         for animale in fence.animals[:]:
              if animale== animal :
                   fence.animals.remove(animal) 
                   fence.area+= animal.area
         
          

            

    def feed(self,animal:Animal):# do da mangiare all'animale e aumento lo spazio occupato
          
          if animal.fence:
               area_richiesta = round((animal.height * 1.02) * (animal.width * 1.02),3) # salvo l'area richiesta in una variabile per prendere l'area che aggiungo
               area_aggiunta= area_richiesta - animal.area  
               if animal.fence.area - area_aggiunta >=0: #controllo se  togliendo l'area aggiunta 
                    
                    animal.health *= 1.01
                    animal.height *= 1.02
                    animal.width *= 1.02 
                    animal.area = area_richiesta # assegno ad animal.area il valore aggiornato 
                    animal.fence.area -= area_aggiunta # tolgo l'area aggiunta all'area della fence

    def clean(self,fence:Fence): #creo una funzione che pulisce la fence
          tempo_di_pulizia: float = 0.0 
          if fence.area == 0:# Se l'area residua è pari a 0 restituisco l'area occupata
               tempo_di_pulizia = fence.area_totale
          else:
                tempo_di_pulizia += round( (( sum(animal.area for animal in fence.animals) )/ fence.area ),3)# Il tempo di pulizia è il rapporto dell'area occupata dagli animali diviso l'area residua del recinto
          return tempo_di_pulizia # ritorno il tempo impiegato per la pulizia
       


class Zoo:
    def __init__(self, fences: list  [Fence], zoo_keepers: list [Zookeeper]):#passo una lista di keepers e di fences
          self.fences = fences
          self.keepers = zoo_keepers

    def describe_zoo(self): # creo una funzione che descrive il mio zoo
          
          print("Guardiani:")
          for keeper in self.keepers: #faccio scorrere la lista di keeper fornita e per ognuno stampo le sue caratteristiche principali
               print(f"Zookeeper (name={keeper.name} , surname= {keeper.surname} , id={keeper.id}") 
          print("Fences:")
          for fence in self.fences: # faccio la stessa cosa con fence
               print(f"Fence (area= {round(fence.area_totale)}, temperatura={fence.temperature}, habitat={fence.habitat})")
               
               print(f"With animals:")
               for animal in fence.animals:# faccio scorrere la lista di animali all'interno di fence 
                    print(f"Animal({Animal.__str__(animal)})")# per ogni animale stampo le caratteristiche prendendo lo __str__ presente nella classe Animal
               print("#"*30) #stampo 30 # per dividere una fence dall'altra
          


       

