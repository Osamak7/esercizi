"""
Creaiamo un sistema di gestione di uno zoo virtuale

Sistema di gestione dello zoo virtuale

Classi:

1. Zoo: questa classe rappresenta uno zoo. Lo zoo ha dei recinti fences e dei guardiani dello zoo, zoo_keepers.

2. Animal: questa classe rappresenta un animale nello zoo. Ogni animale ha questi attributi: name, species, 
age, height, width, preferred_habitat, health h che è uguale a round(100 * (1 / age), 3).

3. Fence: questa classe rappresenta un recinto dello zoo in cui sono tenuti gli animali. I recinti 
possono contenere uno o più animali. I recinti possono hanno gli attributi area, temperature e habitat.

4. ZooKeeper: questa classe rappresenta un guardiano dello zoo responsabile della gestione dello zoo. 
I guardiani dello zoo hanno un nome, un cognome, e un id. Essi possono nutrire gli animali, pulire i recinti e svolgere altri compiti nel nostro zoo virtuale."""

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

    def __str__(self) -> str:
         return f"Animal (name={self.name} , species={self.species} , age={self.age}"




class Zookeeper:
    def __init__(self, name: str, surname: str, id: str):
        self.name = name
        self.surname = surname
        self.id = id
        

    def add_animal(self, animal: Animal, fence: Fence):
        if animal.preferred_habitat == fence.habitat and fence.area - animal.area >= 0:
            fence.animals.append(animal)
            fence.area -= animal.area
            animal.fence=fence

    def remove_animal(self ,animal: Animal, fence: Fence):
         for animale in fence.animals[:]:
              if animale== animal :
                   fence.animals.remove(animal) 
            

    def feed(self,animal:Animal):
          
          if animal.fence:
               area_richiesta = round((animal.height * 1.02) * (animal.width * 1.02),3)
               if animal.fence.area - area_richiesta >=0: 
                    
                    animal.health *= 1.01
                    animal.height *= 1.02
                    animal.width *= 1.02
                    area_aggiunta = area_richiesta - animal.area  
                    animal.area = area_richiesta
                    animal.fence.area -= area_aggiunta

    def clean(self,fence:Fence):
          tempo_di_pulizia: float = 0.0 
          if fence.area == 0:
               tempo_di_pulizia = fence.area_totale
          else:
                tempo_di_pulizia += round( (( sum(animal.area for animal in fence.animals) )/ fence.area ),3)
          return tempo_di_pulizia
       


class Zoo:
    def __init__(self, fences: list  [Fence], zoo_keepers: list [Zookeeper]):
          self.fences = fences
          self.keepers = zoo_keepers

    def describe_zoo(self):
          
          print("Guardiani:")
          for keeper in self.keepers:
               print(f"Zookeeper (name={keeper.name} , surname= {keeper.surname} , id={keeper.id}") 
          print("Fences:")
          for fence in self.fences:
               print(f"Fence (area= {round(fence.area,3)}, temperatura={fence.temperature}, habitat={fence.habitat})")
               
               print(f"With animals:")
               for animal in fence.animals:
                    print(f"Animal({Animal.__str__(animal)})")
               print("#"*30)
          


       


# Esempio di utilizzo:
pippo = Animal(name="Paperino", species="cane", age=12, height=1.10, width=1.20, preferred_habitat="mediterraneo")
fafa = Animal(name="fafa", species="gatto", age=12, height=1.10, width=1.20, preferred_habitat="deserto")
bubu = Animal(name="bubu", species="coniglio", age=12, height=1.10, width=1.20, preferred_habitat="polare")
habitat1 = Fence(area=100.00, temperature=20, habitat="mediterraneo")
habitat2 = Fence(area=200.00, temperature=28, habitat="deserto")
habitat3 = Fence(area=300.00, temperature=29, habitat="polare")

marco = Zookeeper(name="Marco", surname="Rossi", id="kfiewo23")
paolo = Zookeeper(name="paolo", surname="Neri", id="lksdnflqepèac")
maooo =  Animal(name="maaaaaooo", species="t-rex", age=22, height=2.10, width=4.20, preferred_habitat="mediterraneo")
pippo = Animal(name="Paperino1", species="cane", age=12, height=1.10, width=1.20, preferred_habitat="mediterraneo")
pippo2 = Animal(name="Paperino2", species="cane", age=12, height=1.10, width=1.20, preferred_habitat="mediterraneo")
pippo3 = Animal(name="Paperino3", species="cane", age=12, height=1.10, width=1.20, preferred_habitat="mediterraneo")

francesco = Zookeeper(name="francesco", surname="Poldo", id="kjbefkjbaekjbf")
marco.add_animal(pippo, habitat1)
marco.add_animal(pippo2, habitat1)
marco.add_animal(pippo3, habitat1)

marco.add_animal(maooo, habitat1)

marco.add_animal(fafa, habitat2)
marco.add_animal(bubu, habitat3)

marco.clean(habitat1)
print(f"Cleaning time prima: {marco.clean(habitat1)}")
print(pippo.area)
print(habitat1.area)
for i in range(1000000):
     marco.feed(pippo)
print(habitat1.area)

marco.clean(habitat1)

print(f"Cleaning time dopo: {marco.clean(habitat1)}")
o =  Animal(name="o", species="t-rex", age=22, height=2.10, width=4.20, preferred_habitat="mediterraneo")
o1 = Animal(name="o1", species="cane", age=12, height=15, width=10, preferred_habitat="mediterraneo")

marco.add_animal(o,habitat1)
marco.add_animal(o1,habitat1)


marco.add_animal(o,habitat2)
marco.add_animal(o1,habitat3)

z1=Zoo([habitat1,habitat2,habitat3],[marco,paolo,francesco])
z1.describe_zoo()




"""4. clean(fence: Fence) (Pulizia dei recinti): implementare un metodo che consenta 
al guardiano dello zoo di pulire tutti i recinti dello zoo. Questo metodo restituisce un
 valore di tipo float che indica il tempo che il guardiano impiega per pulire il recinto. 
 Il tempo di pulizia è il rapporto dell'area occupata dagli animali diviso l'area residua 
 del recinto. Se l'area residua è pari a 0, restituire l'area occupata."""


"""Funzionalità:

1. add_animal(animal: Animal, fence: Fence) (Aggiungi nuovo animale): 
consente al guardiano dello zoo di aggiungere un nuovo animale allo zoo.
 L'animale deve essere collocato in un recinto adeguato in base alle esigenze 
 del suo habitat e se c'è ancora spazio nel recinto, ovvero se l'area del recinto 
 è ancora sufficiente per ospitare questo animale."""

"""2. remove_animal(animal: Animal, fence: Fence) (Rimuovi animale): consente al guardiano dello zoo
 di rimuovere un animale dallo zoo. L'animale deve essere allontanato dal suo recinto. Nota bene: L'area del 
 recinto deve essere ripristinata dello spazio che l'animale rimosso occupava.

3. feed(animal: Animal) (Dai da mangiare agli animali): implementa un metodo che consenta al guardiano dello zoo di nutrire tutti gli 
animali dello zoo. Ogni volta che un animale viene nutrito, la sua salute incrementa di 1% rispetto alla sua salute corrente, 
ma le dimensioni dell'animale (height e width) vengono incrementate del 2%. Perciò, l'animale si può nutrire soltanto se il recinto 
ha ancora spazio a sufficienza per ospitare l'animale ingrandito dal cibo.

4. clean(fence: Fence) (Pulizia dei recinti): implementare un metodo che consenta al guardiano dello zoo di pulire tutti i recinti dello zoo.
 Questo metodo restituisce un valore di tipo float che indica il tempo che il guardiano impiega per pulire il recinto. Il tempo di pulizia 
 è il rapporto dell'area occupata dagli animali diviso l'area residua del recinto. Se l'area residua è pari a 0, restituire l'area occupata.

5. describe_zoo() (Visualizza informazioni sullo zoo): visualizza informazioni su tutti i guardani dello zoo, sui recinti dello zoo che contengono animali. 

"""