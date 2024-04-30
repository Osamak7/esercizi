from utility import fabbricatore_macchina


"""8-1. Message: Write a function called display_message() that prints one sentence telling 
everyone what you are learning about in this chapter. Call the function, and make sure the message displays correctly."""

def display_message(cosa_ho_imparato:str="""le funzioni,  le liste , i dizionari , le tuple , come interrogarli , modificare quelli che si possono modificare , etcc ...."""):
            return f"in questo periodo abbiamo ripassato: {cosa_ho_imparato}"
print(display_message())

"""8-2. Favorite Book: Write a function called favorite_book() that accepts one parameter,
 title. The function should print a message, such as "One of my favorite books is Alice in Wonderland".
   Call the function, making sure to include a book title as an argument in the function call."""

def favorite_book(a:str):
    return f"uno dei miei libri preferiti è {a}"

print(favorite_book(input("inserisci il tuo libro preferito : ")))

"""8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the text of a message
 that should be printed on the shirt. The function should print a sentence summarizing the size
   of the shirt and the message printed on it. Call the function once using positional arguments
     to make a shirt. Call the function a second time using keyword arguments."""

def make_shirt(taglia:str, scritta:str):
        return f"la taglia che hai scelto è {taglia} con una scritta che dice \"{scritta}\""

print(make_shirt("xl", "joker"))
    
print(make_shirt(scritta="wakanda" , taglia="m" ))

print("\n")

"""8-4. Large Shirts: Modify the make_shirt() function so that shirts are large by default with
 a message that reads I love Python. Make a large shirt and a medium shirt with the default message,
   and a shirt of any size with a different message."""

def new_make_shirt(taglia:str="xxxl", scritta:str="i love python"):
        return f"la taglia della maglietta è {taglia} con una scritta che dice \"{scritta}\""

print(new_make_shirt("l"))
print(new_make_shirt("m"))
print(new_make_shirt(scritta="joker"))

print("\n")

"""8-5. Cities: Write a function called describe_city() that accepts the name of a city and its country.
 The function should print a simple sentence, such as Reykjavik is in Iceland. Give the parameter for the 
 country a default value. Call your function for three different cities, at least one of which is not in the default country."""


def describe_city(name_city:str,country:str="Italy"):
        return f"the name of this city is {name_city} and it is located in {country} " #ci provo in inglese 
print(describe_city("Roma"))
print(describe_city("Milano"))
print(describe_city("Casablanca","Marocco"))
print("\n")


"""8-6. City Names: Write a function called city_country() that takes in the name of a city and its country. 
The function should return a string formatted like this:
 "Santiago, Chile". Call your function with at least three city-country pairs, and print the values that are returned."""

def city_country(name_city:str,country:str):
        return f"{name_city} , {country}"
print(city_country("Catania","Italy"))
print(city_country("Reggio Calabria","Italy"))
print(city_country("Fes","Marocco"))

print("\n")

"""8-7. Album: Write a function called make_album() that builds a dictionary describing a music album. The function 
should take in an artist name and an album title, and it should return a dictionary containing these two pieces of 
information. Use the function to make three dictionaries representing different albums. Print each return value to 
show that the  dictionaries are storing the album information correctly. Use None to add an optional parameter to 
make_album() that allows you to store the number of songs on an album. If the calling line includes a value for the 
number of songs, add that value to the album’s dictionary. Make at least one new function call that includes the number of songs on an album."""

def make_album(artist:str,album_name:str, num_song:int=None):
        pass
        album_musicale:dict[str]={"name artist " :  artist  , "name album " : album_name}
        if num_song:
                album_musicale["number of song"] = num_song
        return f"{album_musicale}"

print(make_album("Linkin Park", "hybrid theory"))
print(make_album("ET", "Telefono casa"))
print(make_album("Drake", "Scorpion",25))
print("\n")


"""8-8. User Albums: Start with your program from Exercise 8-7. Write a while loop that allows users to 
enter an album’s artist and title. Once you have that information, call make_album() with the user’s input and print
 the dictionary that’s created. Be sure to include a quit value in the while loop."""

artista:str=""
album:str=""
while artista == "" :
        artista=input("inserisci il nome di un cantante : ")
        while album=="":
            album=input("inserisci un suo album : ")

print(make_album(artista,album))
       
print("\n")

"""8-9. Messages: Make a list containing a series of short text messages. Pass the list to a function called show_messages(), which prints each text message."""

list_message:list[str]=["Hello world","ciao mondo","this is the list","questa e la lista"]

def show_message(list_message):
        conto:int=1
        for messaggio in list_message:
            print( f"message {conto} = {messaggio}")
            conto +=1
show_message(list_message)

"""8-10. Sending Messages: Start with a copy of your program from Exercise 8-9.
 Write a function called send_messages() that prints each text message and moves each message
   to a new list called sent_messages as it’s printed. After calling the function, print both of your 
   lists to make sure the messages were moved correctly."""

list_message:list[str]=["Hello world","ciao mondo","this is the list","questa e la lista"]

def send_message(list_message):
       
        sent_messages:list[str] = []
        for messaggio in list_message[:]: # itero una copia della lista per poter eliminarli dalla lista che devo iterare ma prima li copio nella nuova lista
              print(messaggio)
              sent_messages.append(messaggio)
              list_message.remove(messaggio)
        print(f"lista messaggi inviati: {sent_messages}")
        print(f"lista messaggi originale : {list_message}")
       
send_message(list_message)
print("\n")
"""8-11. Archived Messages: Start with your work from Exercise 8-10. Call the function send_messages() 
with a copy of the list of messages. After calling the function, print both of your lists to show that the original list has retained its messages."""

list_message:list[str]=["Hello world","ciao mondo","this is the list","questa e la lista"]

def send_message(list_message):
       
        sent_messages:list[str] = []
        for messaggio in list_message: # a differenza del 8.10 qui non devo spostare i messaggi ma devo solo copiare  e stampare
              print(messaggio)
              sent_messages.append(messaggio)
              
        print(f"lista messaggi inviati: {sent_messages}")
        print(f"lista messaggi originale : {list_message}")
       
send_message(list_message)
print("\n")

"""8-12. Sandwiches: Write a function that accepts a list of items a person wants on a sandwich.
 The function should have one parameter that collects as many items as the function call provides,
   and it should print a summary of the sandwich that’s being ordered. Call the function three times,
     using a different number of arguments each time."""



def ingredienti(quantita:int ):
       lista_ingredienti:list[str]= [input("inserisci l'ingrediente : ") for ingrediente in range(quantita) ]
       return f"la lista degli ingredienti del tuo panino è : {lista_ingredienti} \n "

print ( ingredienti ( int ( input ("inserisci la quantita di ingredienti che vuoi nel panino : "))))
print ( ingredienti ( int ( input ("inserisci la quantita di ingredienti che vuoi nel panino : "))))
print ( ingredienti ( int ( input ("inserisci la quantita di ingredienti che vuoi nel panino : "))))

#modo alternativo  :
# quantita_persone:int = int(input ("quante persone siete : ") )
# contatore:int=1
# for persona in range(quantita_persone):
#        nome:str=input(f"ciao sei la persona numero {contatore} come ti chiami : ")
#        print ( ingredienti ( int ( input (f"ciao {nome} inserisci la quantita di ingredienti che vuoi nel panino : "))))
#        contatore+=1

"""8-13. User Profile:  Build a profile of yourself by calling build_profile(),
 using your first and last names and three other key-value pairs that describe you.
   All the values must be passed to the function as parameters. The function then must return
     a string such as "Eric Crow, age 45, hair brown, weight 67"""
print("\n")

def build_profile(nome:str, cognome:str , eta:str, colore_capelli:str , altezza:str ):
        profilo :dict[str]= {
        "nome": nome ,
        "cognome": cognome,
        "eta": eta,
        "colore capelli": colore_capelli,
        "altezza": altezza
        }
        print(f"utente : {profilo['nome']} {profilo['cognome']}, età {profilo['eta']}, colore capelli {profilo['colore capelli']} , altezza {profilo['altezza']}")
        
build_profile("ET", "L'alieno", "21", "castani" , "180 cm") 



"""8-14. Cars: Write a function that stores information about a car in a dictionary. 
The function should always receive a manufacturer and a model name. It should then accept an arbitrary 
number of keyword arguments. Call the function with the required information and two other name-value pairs,
 such as a color or an optional feature. Your function should work for a call like this one:
   car = make_car('subaru', 'outback', color='blue', tow_package=True) Print the dictionary that’s 
   returned to make sure all the information was stored correctly.""" 
   
print("\n")

def make_car(casa_produtrice: str, modello: str, **caratteristiche: str) -> dict:
    info_macchina: dict[str] = {
        "casa produtrice": casa_produtrice,
        "modello": modello
    }
    info_macchina.update(caratteristiche)
    return info_macchina

car = make_car('mustang', 'gt', colore ='nero opaco' , tettuccio = "decappottabile" , anno = "2018")
print(car)

"""8-15. Printing Models: Put the functions for the example printing_models.py in 
a separate file called printing_functions.py. Write an import statement at the top 
of printing_models.py, and modify the file to use the imported functions."""
print("\n")


car = fabbricatore_macchina('audi', 'Q7', colore ='nero e arancione'  , anno = "2022")
print(car)

print("\n")
"""8-16. Imports: Using a program you wrote that has one function in it, store that function in a separate file.
 Import the function into your main program file, and call the function using each of these approaches:
import module_name
from module_name import function_name
from module_name import function_name as fn
import module_name as mn
from module_name import *"""

import utility     #importo il file
car = utility.fabbricatore_macchina('audi', 'Q7', colore ='nero e arancione'  , anno = "2022")
print(car)


from utility import fabbricatore_macchina               # importo la funzione dal file 
car = fabbricatore_macchina('audi', 'Q7', colore ='nero e arancione'  , anno = "2022")
print(car)


from utility import fabbricatore_macchina as creo_macchina              #importo la funzione e gli do un alto nome
car = creo_macchina('audi', 'Q7', colore ='nero e arancione'  , anno = "2022")
print(car)


import utility as fabbricatore_macchina #importo il file come il nome della funzione 
car = fabbricatore_macchina.fabbricatore_macchina('audi', 'Q7', colore='nero e arancione', anno="2022")
print(car)


from utility import * # importo tutto da utility
car = fabbricatore_macchina('audi', 'Q7', colore ='nero e arancione'  , anno = "2022")
print(car)


"""8-17. Styling Functions: Choose any three programs you wrote for this chapter,
 and make sure they follow the styling guidelines described in this section."""
print("\n")
#1
def display_message ( cosa_ho_imparato : str = """le funzioni , 
                                        le liste , 
                                        i dizionari , 
                                        le tuple , 
                                        etcc ....""") -> str :
            
        return f"in questo periodo abbiamo ripassato: {cosa_ho_imparato}"

print( display_message() )


#2
def city_country( name_city : str , country : str ) -> str :
        
        return f"{ name_city } , { country } "

print ( city_country ( "Catania" , "Italy" ) )
print ( city_country ( "Reggio Calabria" , "Italy" ) )
print ( city_country ( "Fes" , "Marocco" ) )




#3
def make_shirt ( taglia : str , scritta : str ) -> str :
        return f"La taglia che hai scelto è { taglia } con una scritta che dice \"{ scritta }\" "

print ( make_shirt ( "xl" , "joker" ) )