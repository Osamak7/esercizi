#Oussama hliwa
#18/04/2024

"""2-3. Personal Message: Use a variable to represent a person’s name,
and print a message to that person. Your message should
be simple, such as, “Hello Eric, would you like to learn some Python today?”"""

nome:str="Piero"
print(f"ciao {nome}, ti va di imparare python insieme oggi ? ")

"""2-4. Name Cases: Use a variable to represent a person’s name, 
and then print that person’s name in lowercase, uppercase, and title case."""

nome_utente:str="Luigi"
nome_upper:str=nome_utente.upper()
print(nome_upper)
nome_lower:str=nome_utente.lower()
print(nome_lower)
nome_title:str=nome_utente.title()
print(nome_title)

"""2-5. Famous Quote: Find a quote from a famous person you admire. Print the quote and the name of its author. 
Your output should look something like the following, 
including the quotation marks: Albert Einstein once said, “A person who never made a mistake never tried anything new.”"""

frase_famosa:str="Giulio Cesare una volta disse \" Il dado è tratto\""
print(frase_famosa)

"""2-6. Famous Quote 2: Repeat Exercise 2-5, but this time, represent the famous person’s name using a variable
 called famous_person. Then compose your message and represent it with a new variable called message. Print your message. """

persoa_famose:str="Albert Einstein"
frase_famosa:str="\" Non hai veramente capito qualcosa fino a quando non sei in grado di spiegarlo a tua nonna \""
print(f"{persoa_famose} una volta disse {frase_famosa}")

"""2-8. File Extensions: Python has a removesuffix() method that works exactly like removeprefix(). Assign the value 'python_notes.txt' 
to a variable called filename. Then use the removesuffix() method to display the filename without the file extension, like some file browsers do."""

nome_file:str="python_notes.txt"
nome_file=nome_file.removesuffix(".txt")
print(nome_file)

"""3-1. Names: Store the names of a few of your friends in a list called names. Print each person’s name by accessing
 each element in the list, one at a time."""
 
lista_nomi:list=["Berlusconi","Paperon de Paperoni","Totti"]
for i in lista_nomi:
    print(i)

"""3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just printing each person’s name,
 print a message to them. The text of each message should be the same, but each message should be personalized with the person’s name."""

for i in lista_nomi:
    print(f"{i} ciao come stai ?")

""""3-3. Your Own List: Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples.
 Use your list to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”"""

auto:list=["vorrei possedere una lamborghini","mi piacerebbe possedere una ferrari ", "mi stuzzicherebbe avere una pagani"]
for i in auto:
    print(i)

"""3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes 
at least three people you’d like to invite to dinner. Then use your list to print a message to each person, inviting them to dinner."""

lista_invitati:list=["Bill Gates","Warren Buffet","Cristino Ronaldo"]
for n in lista_invitati:
    print(f"Ciao {n} vorrei invitarti per avere un confronto e dei suggerimenti riguardo al futuro")

"""3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, 
so you need to send out a new set of invitations. You’ll have to think of someone else to invite.
• Start with your program from Exercise 3-4. Add a print() call at the end of your program, stating the name of the guest who can’t make it.
• Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
• Print a second set of invitat"""

non_puo_venire:str=lista_invitati.pop(1)
print(f"{non_puo_venire} ha appena comunicato che non ci sarà")
nuovo_invitato:str="Pogba"
lista_invitati.append(nuovo_invitato)
print(lista_invitati)
for n in lista_invitati:
    print(f"Ciao {n} vorrei invitarti per avere un confronto e dei suggerimenti riguardo al futuro")


"""
3-6. More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
• Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your program, informing people that you found a bigger table.
• Use insert() to add one new guest to the beginning of your list.
• Use insert() to add one new guest to the middle of your list.
• Use append() to add one new guest to the end of your list.
• Print a new set of invitation messages, one for each person in your list."""

print("ho appena trovato un tavolo più grande per invitare nuovi invitati ")
lista_invitati.insert(1,"Matuidi")
lista_invitati.insert(2,"Zidan")
lista_invitati.append("M.Jordan")
print(lista_invitati)
for n in lista_invitati:
    print(f"Ciao {n} vorrei invitarti per avere un confronto e dei suggerimenti riguardo al futuro")

"""3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and now you have space for only two guests.
• Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
• Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to
 that person letting them know you’re sorry you can’t invite them to dinner.
• Print a message to each of the two people still on your list, letting them know they’re still invited.
• Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program."""


print("il tavolo non sarà più disponibile per cena ora ci sono solo due posti a disposizione ")
print(lista_invitati)
while len(lista_invitati)>2:
    print(f"{lista_invitati[0]} mi dispiace non poterti invitare alla mia cena")
    lista_invitati.pop(0)
print(lista_invitati)
for i in lista_invitati:
    print(f"{i} ti confermo che sei ancora invitato")
del(lista_invitati[0:])
print(lista_invitati)


"""3-8. Seeing the World: Think of at least five places in the world you’d like to visit.
• Store the locations in a list. Make sure the list is not in alphabetical order.
• Print your list in its original order. Don’t worry about printing the list neatly; just print it as a raw Python list.
• Use sorted() to print your list in alphabetical order without modifying the actual list.
• Show that your list is still in its original order by printing it.
• Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.
• Show that your list is still in its original order by printing it again.
• Use reverse()  to change the order of your list. Print the list to show that its order has changed.
• Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
• Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
• Use sort() to change your list so it’s stored in reverse-alphabetical order.
Print the list to show that its order has changed."""

posti_da_visitare:list=["NY","Tokyo","San Paolo","Montecarlo","Singapore"]
print("lista originale : ",posti_da_visitare)
print("lista ordinata  ma non aggiornata :" ,sorted(posti_da_visitare))
print("lista originale : ",posti_da_visitare)

print("ordinata in alfabeto inverso : ",sorted(posti_da_visitare, reverse=True))
print("lista originale : ",posti_da_visitare)

print("far vedere che la lista non è cambiata :",posti_da_visitare)
posti_da_visitare.reverse()
print(posti_da_visitare)
posti_da_visitare.reverse()
print(posti_da_visitare)
posti_da_visitare=sorted(posti_da_visitare)
print(posti_da_visitare)
posti_da_visitare=sorted(posti_da_visitare,reverse=True)
print(posti_da_visitare)

"""3-9. Dinner Guests: Working with one of the programs from Exercises 3, use len() 
to print a message indicating the number of people you’re inviting to dinner."""

print(f"numero di persone invitate a cena : {len(lista_nomi)}")


"""3-10. Every Function: Think of things you could store in a list. For example, you could make a list of mountains, 
rivers, countries, cities, languages, or anything else you’d like. Write a program that creates a list containing these
items and then uses each function introduced in this chapter at least once."""

def genera_lista():
    paesi:list=["Inghilterra","America","Australia","China","Vietnam","Spagna","Canada"]
    nuovo_stato:str = "Brasile.com"
    nuovo_stato : str = nuovo_stato.removesuffix(".com")
    paesi.append(nuovo_stato)
    paesi.insert(1,"Marocco")
    paesi.pop(3)
    paesi = sorted(paesi,reverse=True)
    paesi2 : list [str] =[]
    print(paesi)

    for paese in paesi:
        if paese == "America":
            paesi.remove("America")
        stato : str = paese.upper()
        paesi2.append(stato)

    del(paesi)

    print(paesi2)

   

genera_lista()

"""6-1. Person: Use a dictionary to store information about a person you know.
Store their first name, last name, age, and the city in which they live. You should have keys such as first_name, last_name,
age, and city. Print each piece of information stored in your dictionary."""
person:dict={"Name":"Gigi","Surname":"Rossi","Age":30,"City":"Milano"}
chiavi=person.keys()
for key in chiavi:
    print(f"{key} : {person[key]}")


"""6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers. Think of five names,
and use them as keys in your dictionary. Think of a favorite number for each person, and store each 
as a value in your dictionary. Print each person’s name and their favorite number. For even more fun, 
poll a few friends and get some actual data for your program."""
favorite_numbers:dict={"Mario":3,"Luigi":27,"Pietro":"6","Momo":7,"Lollo":9}
chiavi=favorite_numbers.keys()
for key in chiavi:
    print(f"{key} : {favorite_numbers[key]}") 

"""6-3. Glossary: A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
• Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store their meanings as values.
• Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning,
or print the word on one line and then print its meaning indented on a second line. 
Use the newline character (\n) to insert a blank line between each word-meaning pair in your output."""
glossary:dict={"Function":"Sono blocchi di codice riutilizzabili che eseguono un insieme specifico di istruzioni quando vengono chiamati",
               "Tuple":"sono elementi sequenziali costituiti da una concatenazione di valori di qualsiasi tipo, ognuno memorizzato per posizione",
               "List":"rappresentano una struttura dati sequenziale che memorizza gli elementi in un determinato ordine, ammette duplicati e permette di modificare gli oggetti che contiene",
               "dict":"sono un tipo built-in, mutabile e non ordinato che contiene elementi (items) formati da una chiave (key) e un valore (value)",
               "Print":"permette di scrivere sulla vostra console delle stringhe (sequenze di caratteri)."}
chiavi=glossary.keys()
for key in chiavi:
    print(f"{key} : {glossary[key]}\n") 
    


"""6-7. People: Start with the program you wrote for Exercise 6-1. Make two new dictionaries representing different people,
and store all three dictionaries in a list called people. Loop through your list of people. As you loop through the list, 
print everything you know about each person."""

lista_persone:dict={"Mario":{"Cittadinanza":"Italiano","eta":21,"Altezza":170},
                    "Luigi":{"Cittadinanza":"Bulgaria","eta":26,"Altezza":160},
                    "Pietro":{"Cittadinanza":"Italiano","eta":25,"Altezza":173},
                    "Momo":{"Cittadinanza":"Marocchino","eta":23,"Altezza":180}}

lista_pers2 : dict = {"Piero":{"Cittadinanza":"Italiano","eta":40,"Altezza":179},
                    "Lucrezia":{"Cittadinanza":"Bulgaria","eta":32,"Altezza":172},
                    "Lorenzo":{"Cittadinanza":"Italiano","eta":26,"Altezza":175},
                    "Omar":{"Cittadinanza":"Marocchino","eta":29,"Altezza":183}}

persone : list =[lista_persone,lista_pers2]
for dizionario in persone:
    for k,v in dizionario.items():
        print((f"{k}"))
        for k1, v1 in v.items():
            print(f"     {k1},{v1}")



"""6-8. Pets: Make several dictionaries, where each dictionary represents a different pet.
 In each dictionary, include the kind of animal and the owner’s name. Store these dictionaries
 in a list called pets. Next, loop through your list and as
you do, print everything you know about each pet. """

pets:dict={"cane": {"razza":"alano","nome":"thor"},
           "gatto":{"razza":"siamese","nome":"loki"}}

pets2:dict={"criceto":{"razza":"siberiano","nome":"floky"},
            "serpente":{"razza":"boa","nome":"jormungard"}}

lista_animali:list=[pets,pets2]
for dizionario in lista_animali:
    for chiave,valore in dizionario.items():
        print(f"{chiave}:")
        for chiave1,valore1 in valore.items():
            print(f"     {chiave1}: {valore1}")

"""6-9. Favorite Places: Make a dictionary called favorite_places. 
Think of three names to use as keys in the dictionary, and store one to three favorite places for each person. 
To make this exercise a bit more interesting, ask some friends to name a few of their favorite places.
 Loop through the dictionary, and print each person’s name and their favorite places."""

#create a dictionary with pesron and for each person in the dictionary ask how many favorite seats they have and use this number to 
# generate a loop with that range and enter the favorite seat for how many numbers in the range

lista_persone: dict ={"Marco":{"numero posti preferiti"  : ""  , "posti preferiti":[]},
                      "Luigi":{"numero posti preferiti"  : ""  , "posti preferiti":[]},
                      "Matteo":{"numero posti preferiti" : ""  , "posti preferiti":[]}}

for nome,valori in lista_persone.items():
   valori["numero posti preferiti"]= int(input(f"{nome} inserisci il numero di posti che vuoi inserire : "))

   for i in range (valori["numero posti preferiti"]) :
        valori["posti preferiti"].append(input(f"{nome} inserisci il  tuo {i+1} posti preferiti: "))
 
for k,v in lista_persone.items():
    print(k)
    for k1,v1 in v.items():
        print(f"       {k1}  :  {v1} ")

    




"""6-10. Favorite Numbers: Modify your program from Exercise 6-2 so each person can have more than one favorite number. 
Then print each person’s name along with their favorite numbers."""

favorite_numbers:dict={"Mario":{"favorite numbers":[2,3,4,5]}, 
                       "Luigi":{"favorite numbers":[4,5,6,7]}, 
                       "Pietro":{"favorite numbers":[1,2,32]},
                       "Momo":{"favorite numbers":[7,77,777]}, 
                       "Lollo":{"favorite numbers":[0,9,8,7]}}
for k,v in favorite_numbers.items():
    print(f"{k}")
    for k1,v1 in v.items():
        print(f"        {k1} : {v1}")


"""6-11. Cities: Make a dictionary called cities. Use the names of three cities as keys in your dictionary.
 Create a dictionary of information about each city and include the country that the city is in, 
 its approximate population, and one fact about that city. The keys for each city’s dictionary should be something 
 like country, population, and fact. Print the name of each city and all of the information you have stored about it."""

cities:dict={"Roma":{"country":"Italy", "population":" 2 754 228 abitanti ","fact":"è il comune più popoloso d'Italia   "},
            "Casablanca":{"country":"Maroc", "population":"  4 250 050 ","fact":"  Casablanca è la più grande città del Marocco.  "},
            "Rio de janeiro":{"country":"Brazil", "population":" 6 688 930 ","fact":" È famosa per le sue attrattive turistiche come la spiaggia di copacabana"} } 

for k,v in cities.items():
    print(f"{k}")
    for k1,v1 in v.items():
        print(f"        {k1} : {v1}")
    

"""6-12. Extensions: We’re now working with examples that are complex enough that they 
can be extended in any number of ways. Use one of the example programs from this chapter,
 and extend it by adding new keys and values, changing the context of the program, or improving the formatting of the output."""

print("\n")

cities:dict={"Roma":
            {"continente":"Europa", "country":"Italy","lingua ufficiale":"italiano", "population":" 2 754 228 abitanti ","fact":"è il comune più popoloso d'Italia   "},
            "Casablanca":
            {"continente":"Africa", "country":"Maroc","lingua ufficiale":"marocchino", "population":"  4 250 050 ","fact":"  Casablanca è la più grande città del Marocco.  "},
            "Rio de janeiro":
            {"contiinente":"America meridionale","country":"Brazil","lingua ufficiale":"portoghese", "population":" 6 688 930 ","fact":" È famosa per le sue attrattive turistiche come la spiaggia di copacabana"} } 

for k,v in cities.items():
    print(f"{k}:")
    for k1,v1 in v.items():
        print(f"        {k1} : {v1}")
    print("\n")
