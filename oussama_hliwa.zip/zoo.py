"""
Creaiamo un sistema di gestione di uno zoo virtuale

Sistema di gestione dello zoo virtuale

Classi:

1. Zoo: questa classe rappresenta uno zoo. Lo zoo ha dei recinti fences e dei guardiani dello zoo, zoo_keepers.

2. Animal: questa classe rappresenta un animale nello zoo. Ogni animale ha questi attributi: name, species, 
age, height, width, preferred_habitat, health che è uguale a round(100 * (1 / age), 3).

3. Fence: questa classe rappresenta un recinto dello zoo in cui sono tenuti gli animali. I recinti 
possono contenere uno o più animali. I recinti possono hanno gli attributi area, temperature e habitat.

4. ZooKeeper: questa classe rappresenta un guardiano dello zoo responsabile della gestione dello zoo. 
I guardiani dello zoo hanno un nome, un cognome, e un id. Essi possono nutrire gli animali, pulire i recinti e svolgere altri compiti nel nostro zoo virtuale."""

class Animal:
     def __init__(self, name:str , species:str , age:int , height:float , width:float , preferred_habitat:str 
                    ) :
          self.name=name
          self.species=species
          self.age=age
          self.height=height
          self.width=width
          self.preferrad_habbitat=preferred_habitat
          self.healt=round(100 * (1 / age),3)
          

class Fences:      
    def __init__(self, area : float ,temperature : int , habbitat:str) :
         self.area=area
         self.temperature= temperature
         self.habbitat=habbitat
         
         

class Zookeepers:
     def __init__(self,name:str, surname:str , id :str, animals:list[Animal]=[], fences:list[Fences]=[]) -> None:
          self.name=name
          self.surname=surname
          self.animals:list[Animal]=animals
          self.fences:list[Fences]=fences

     def clean(fences: Fences) :
          for fence in fences[:]:
               pass

     def add_animal(self,animal: Animal, fences: Fences):
          for animale in animal :
               for fence in fences:
                    print(animale)
                    if animale.preferrad_habbitat == fence.habbitat  and fence.area - animal.area (animal.height* animal.width) > 0:
                         fences.append(animale)

                         print("ciao",fences)

     def feed(animal: Animal):
          pass


class Zoo:
     def __init__(self, fences : list=[] , zoo_keepers:list=[]) -> None:
        self.fences=fences
        self.zoo_keepers=zoo_keepers
        
    
     def  describe_zoo()  -> str:
          return f"all'interno dello zoo abbiamo {Fences} "
             

pippo=Animal(name="pippo", species="cane", age=12, height=1.10, width=1.20, preferred_habitat="mediterraneo")
habitat1=Fences(area=100.00, temperature=20, habbitat="mediterraneo")
marco=Zookeepers(name="Marco", surname="Rossi", id="kfiewo23")
pollo=Animal("mimmo","pollo",13 ,1.20,1.10,"campagna")
print(pollo.healt)

marco.add_animal(pippo,habitat1)
print(Zookeepers.add_animal)
"""Funzionalità:

1. add_animal(animal: Animal, fence: Fence) (Aggiungi nuovo animale): 
consente al guardiano dello zoo di aggiungere un nuovo animale allo zoo.
 L'animale deve ess
 ere collocato in un recinto adeguato in base alle esigenze 
 del suo habitat e se c'è ancora spazio nel recinto, ovvero se l'area del recinto 
 è ancora sufficiente per ospitare questo animale."""

"""4. clean(fence: Fence) (Pulizia dei recinti): implementare un metodo che consenta 
al guardiano dello zoo di pulire tutti i recinti dello zoo. Questo metodo restituisce un
 valore di tipo float che indica il tempo che il guardiano impiega per pulire il recinto. 
 Il tempo di pulizia è il rapporto dell'area occupata dagli animali diviso l'area residua 
 del recinto. Se l'area residua è pari a 0, restituire l'area occupata."""


"""2. remove_animal(animal: Animal, fence: Fence) (Rimuovi animale): consente al guardiano dello zoo di rimuovere un animale dallo zoo. L'animale deve essere allontanato dal suo recinto. Nota bene: L'area del recinto deve essere ripristinata dello spazio che l'animale rimosso occupava.

3. feed(animal: Animal) (Dai da mangiare agli animali): implementa un metodo che consenta al guardiano dello zoo di nutrire tutti gli animali dello zoo. Ogni volta che un animale viene nutrito, la sua salute incrementa di 1% rispetto alla sua salute corrente, ma le dimensioni dell'animale (height e width) vengono incrementate del 2%. Perciò, l'animale si può nutrire soltanto se il recinto ha ancora spazio a sufficienza per ospitare l'animale ingrandito dal cibo.

4. clean(fence: Fence) (Pulizia dei recinti): implementare un metodo che consenta al guardiano dello zoo di pulire tutti i recinti dello zoo.
 Questo metodo restituisce un valore di tipo float che indica il tempo che il guardiano impiega per pulire il recinto. Il tempo di pulizia 
 è il rapporto dell'area occupata dagli animali diviso l'area residua del recinto. Se l'area residua è pari a 0, restituire l'area occupata.

5. describe_zoo() (Visualizza informazioni sullo zoo): visualizza informazioni su tutti i guardani dello zoo, sui recinti dello zoo che contengono animali. 

"""