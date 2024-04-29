import random

"""4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these pizza names in a list,
 and then use a for loop to print the name of each pizza.
• Modify your for loop to print a sentence using the name of the pizza, instead of printing just the name of the pizza. For each pizza,
   you should have one line of output containing a simple statement like I like pepperoni pizza.
• Add a line at the end of your program, outside the for loop, that states how much you like pizza. 
The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, such as I really love pizza!"""

pizze_preferite:list=["margherita","tonno e cipolla","marinara"]
print(f"le mie pizze preferite sono :")
for pizza in pizze_preferite:
    print(f"                        la pizza {pizza}")
print(f"la classifica delle pizze che mi piace di piu è : 1){pizze_preferite[0]} , 2){pizze_preferite[1]} e in fine 3){pizze_preferite[2]} \n")

"""4-2. Animals: Think of at least three different animals that have a common characteristic. Store the names of these animals in a list, and then use a for loop to print out the name of each animal.
• Modify your program to print a statement about each animal, such as A dog would make a great pet.
• Add a line at the end of your program, stating what these animals have in common. You could print a sentence, such as Any of these animals would make a great pet!"""
animali:list=["cane","gatto","criceto"]
caratteristiche:list=["è un animale molto affettuoso e bisogna prestarli molte cure"," è un animale autonomo ed a volte distaccato ","ha bisogno di compagnia e molta attenzione e cura "]
contatore:int=0
for animale in animali:
    print(f"il {animale} : {caratteristiche[contatore]} ")
    contatore+=1
print(f"ognuno di questi animali : {animali} è un ottimo animale domestico\n")

"""4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive."""
for num in range(1,21):
    print(num)
print("\n")

"""4-4. One Million: Make a list of the numbers from one to one million, and then use a for loop to print the numbers.
 (If the output is taking too long, stop it by pressing CTRL-C or by closing the output window.)"""
lista_numeri:list=[num for num in range(1,1000001)]
# for numero in lista_numeri:
#     print(numero)


"""4-5. Summing a Million: Make a list of the numbers from one to one million, and then use min() and max() 
to make sure your list actually starts at one and ends at one million. Also, use the sum() function to see how quickly Python can add a million numbers."""
million:list=[num for num in range(1,1000001)]
print(f"il minimo è {min(million)} mentre il massimo è {max(million)}")
print(f"la somma dei  dumeri da {min(million)} a {max(million)} è { sum(million)} \n")

"""4-6. Odd Numbers: Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. Use a for loop to print each number."""
num_dispari:list=[ num for num in range (1,21,2)]
for num in num_dispari:
    print(num)
print("\n")

"""4-7. Threes: Make a list of the multiples of 3, from 3 to 30. Use a for loop to print the numbers in your list."""
threes:list=[num for num in range(3,31,3**1)]
for num in threes:
    print(num)
print("\n")


"""4-8. Cubes: A number raised to the third power is called a cube. For example, the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), and use a for loop to print out the value of each cube."""
cubes:list=[num**3 for num in range(1,11)]
contatore:int=1
for num in cubes:
    print(f"il cubo di {contatore} è {num}")
    contatore+=1
print("\n")

"""4-9. Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes."""
cubes:list=[num**3 for num in range(1,11)]
print(f"{cubes}\n")

"""4-10. Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
• Print the message The first three items in the list are:. Then use a slice to print the first three items from that program’s list.
• Print the message Three items from the middle of the list are:. Then use a slice to print three items from the middle of the list.
• Print the message The last three items in the list are:. Then use a slice to print the last three items in the list."""
print(f"primi tre elementi sono: {cubes[0:3]} ")
print(f"i numeri al centro sono 4 : {cubes[3:7]} poiche {len(cubes)} è un numero pari e non sarebbe giusto metterne 3")
print(f"gli ultimi tre elementi della lista sono {cubes[-3:]} ")


"""4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1.
 Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:
• Add a new pizza to the original list.
• Add a different pizza to the list friend_pizzas.
• Prove that you have two separate lists. Print the message My favorite pizzas are:, 
and then use a for loop to print the first list. Print the message My friend’s favorite pizzas are:,
 and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list."""
print("\n")
pizze_preferite:list=["margherita","tonno e cipolla","marinara"]
friend_pizzas:list=pizze_preferite.copy()
pizze_preferite.append("cacio e pepe")
friend_pizzas.append("4 stagioni")
print("le mie pizze preferite sono:")
for pizza in pizze_preferite:
    print(f"                            pizza {pizza}")

print("\nle pizze preferite del mio amico sono :")
for pizza in friend_pizzas:
    print(f"                            pizza {pizza}")

"""4-12. More Loops: All versions of foods.py in this section have avoided using for loops when printing, to save space. Choose a version of foods.py, and write two for loops to print each list of foods."""

foods_py:list=["pollo","pasta","pizza"]
mangiare_py:list=["pane","pomodoro","lenticchie"]
for alimento in foods_py:
    print(alimento)
for alimento in mangiare_py:
    print(alimento)


"""4-14. PEP 8: Look through the original PEP 8 style guide at https://python.org/dev/peps/pep-0008. You won’t use much of it now, but it might be interesting to skim through it."""

"""4-15. Code Review: Choose three of the programs you’ve written in this chapter and modify each one to comply with PEP 8."""
#1
num_dispari:list=[ num for num in range (1,21,2)]
for num in num_dispari:
    print(num)
print("\n")
#2
threes:list=[num for num in range(3,31,3**1)]
for num in threes:
    print(num)
print("\n")

#3
for num in range(1,21):
    print(num)
print("\n")

"""5-1. Conditional Tests: Write a series of conditional tests. Print a statement
describing each test and your prediction for the results of each test. Your code
should look something like this:
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
• Look closely at your results, and make sure you understand why each line
evaluates to True or False.
• Create at least 10 tests. Have at least 5 tests evaluate to True and another
5 tests evaluate to False."""

macchina = "audi"

# Test 1: 
print(f"La macchina è 'audi'?                         {macchina == 'audi'}")

# Test 2: 
print(f"La macchina non è 'subaru'?                   {macchina != 'subaru'}")

# Test 3: 
print(f"La macchina non è 'bmw'?                      {macchina != 'bmw'}")

# Test 4: 
print(f"La macchina è 'BMW'?                          {macchina == 'BMW'}")

# Test 5: 
print(f"La macchina non è 'audi'?                     {macchina != 'audi'}")

# Test 6: 
print(f"La macchina è vuota?                          {macchina == ''}")

# Test 7:
print(f"La macchina è una stringa vuota?              {macchina == ''}")

# Test 8:
print(f"La lunghezza della macchina è maggiore di 0?  {len(macchina) > 0}")

# Test 9:
print(f"La lunghezza della macchina è maggiore di 5?  {len(macchina) > 5}")

# Test 10: 
print(f"La macchina è diversa da 'Audi'?              {macchina != 'Audi'}")

"""5-2. More Conditional Tests: You don’t have to limit the number of tests you cre-
ate to 10. If you want to try more comparisons, write more tests and add them

to conditional_tests.py. Have at least one True and one False result for each of
the following:
• Tests for equality and inequality with strings
• Tests using the lower() method
• Numerical tests involving equality and inequality, greater than and less
than, greater than or equal to, and less than or equal to
• Tests using the and keyword and the or keyword
• Test whether an item is in a list
• Test whether an item is not in a list"""
print("\n")
# uguaglianza di stringhe
print(f"La macchina è 'bmw'?                           {macchina == 'bmw'}")
print(f"La macchina è diversa da 'audi'?               {macchina != 'audi'}")

# usando il metodo lower
print(f"La macchina in minuscolo è 'audi'?             {macchina.lower() == 'audi'}")

# Test numerici che coinvolgono uguaglianza , disuguaglianza, maggiore , minore  e/o uguale 
numero = 777
print(f"Il numero {numero} è uguale a 10?                   {numero == 10}")
print(f"Il numero {numero} è maggiore di 5?                 {numero > 5}")
print(f"Il numero {numero} è minore o uguale a 15?          {numero <= 777}")
print(f"Il numero {numero} è diverso da 7?                  {numero != 7}")

# test utilizzando le parole chiavi :(and , or)
a = 7
b = 27
print(f"{a} è maggiore di 5 e {b} è minore di 25?         {a > 5 and b < 30}")
print(f"{a} è minore di 5 o {b} è maggiore di 15?         {a < 5 or b > 15}")

# test per vedere se un elemento è nella lista 
numbers = [1, 3, 5, 7, 9]
print(f"Il numero 7 è presente nella lista?            {7 in numbers}")
print(f"Il numero 10 non è presente nella lista?       {10 not in numbers}")

"""5-3. Alien Colors #1: Imagine an alien was just shot down in a game. Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
• Write an if statement to test whether the alien’s color is green. If it is, print a message that the player just earned 5 points.
• Write one version of this program that passes the if test and another that fails. (The version that fails will have no output.)"""
alien_color:str="green"
if alien_color is "green":
    print(f"\nhai appena guadagnato 5 punti xp")
if alien_color is "red":
    alien_color="orange"


"""5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.
• If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.
• If the alien’s color isn’t green, print a statement that the player just earned 10 points.
• Write one version of this program that runs the if block and another that runs the else block."""

alien_color:str="green"
i:int=0
while i<2:
    if i==1:
        alien_color="red"
    if alien_color is "green":
        print(f"\nhai appena guadagnato 5 punti xp per aver sparato all'alieno")
    else :
        print("hai appena guadagnato 10 punti \n")
    i+=1

"""5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elif-else chain.

• If the alien is green, print a message that the player earned 5 points.
• If the alien is yellow, print a message that the player earned 10 points.
• If the alien is red, print a message that the player earned 15 points.
• Write three versions of this program, making sure each message is printed for the appropriate color alien."""

colori:list[str]=["green","yellow","red","amaranto"]
i:int=0
while i<len(colori):
    alien_color=colori[i]
    if alien_color is colori[0]:
        print(f"l'alieno è {alien_color} hai appena guadagnato 5 punti ")

    elif alien_color is colori[1]:
        print(f"l'alieno è {alien_color} hai appena guadagnato 10 punti")

    elif alien_color is colori[2]:
        print(f"l'alieno è {alien_color} hai appena guadagnato 15 punti")

    else :
        print(f"l'alieno non è ne rosso ne giallo e ne verde ma è {alien_color}")
    i+=1

"""5-6. Stages of Life: Write an if-elif-else chain that determines a person’s stage of life. Set a value for the variable age, and then:
• If the person is less than 2 years old, print a message that the person is a baby.
• If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
• If the person is at least 4 years old but less than 13, print a message that the person is a kid.
• If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
• If the person is at least 20 years old but less than 65, print a message that the person is an adult.
• If the person is age 65 or older, print a message that the person is an elder."""
print("\n")
eta:int=10
if eta <2 :
    print(f"hai {eta}anni sei un neonato")

elif eta >= 2 and eta < 4:
    print(f"hai {eta} anni sei un bambino piccolo")

elif eta >= 4 and eta  <13:
    print(f" hai {eta} anni sie un bambino in età prescolare") 

elif eta >= 13 and eta <20:
    print(f" hai {eta} anni siu un adolescente") 

elif eta >=20 and eta < 65:
    print(f"hai {eta} anni sei un adulto")

else:
    print(f"hai {eta} anni sei un anziano")
print("\n")

"""5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of independent if statements that check for certain fruits in your list.
• Make a list of your three favorite fruits and call it favorite_fruits.
• Write five if statements. Each should check whether a certain kind of fruit is in your list. If the fruit is in your list, the if block should print a statement, such as You really like Apples!"""

favorite_fruits:list[str]=["mela","fragola","pera","cocco","ananas"]
if "ananas"in favorite_fruits:
    print(f"ti piace davvero l'ananas !")
if "mela" in favorite_fruits:
    print("ti piace davvero la mela !")
if "fragola" in favorite_fruits:
    print("ti piace davvero la fragola !")
if "pera" in favorite_fruits:
    print("ti piace davvero la pera !")
if "cocco" in favorite_fruits:
    print("ti piace davvero il cocco !")

"""5-8. Hello Admin: Make a list of five or more usernames, including the name 'admin'. Imagine you are writing code that will print a greeting to each user after they log in to a website. Loop through the list, and print a greeting to each user.
• If the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report?
• Otherwise, print a generic greeting, such as Hello Jaden, thank you for logging in again."""
print("\n")
lista_utenti:list[str]=["Marco","Frank","admin","Ettore","gìGiulian"]
utente:str=random.choice(lista_utenti) # scelgo un utente casuale dalla lista
if utente is "admin":
    print(f"ciao {utente} desideri un rapporto sulla giornata")
else:
    print(f"ciao e un piacere rivederti {utente}")

"""5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is not empty.
• If the list is empty, print the message We need to find some users!
• Remove all of the usernames from your list, and make sure the correct message is printed."""
lista_utenti.clear()
if len(lista_utenti)==0:
    print(f"non ci sono utenti bisogna cercare nuovi utenti")


"""5-10. Checking Usernames: Do the following to create a program that simulates how websites ensure that everyone has a unique username.
• Make a list of five or more usernames called current_users.
• Make another list of five usernames called new_users. Make sure one or two of the new usernames are also in the current_users list.
• Loop through the new_users list to see if each new username has already been used. If it has, print a message that the person will
 need to enter a new username. If a username has not been used, print a message saying that the username is available.
• Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should not be accepted. (To do this, 
you’ll need to make a copy of current_users containing the lowercase versions of all existing users.)"""

print("\n")
current_user:list[str]=["amin","asaf","luigi","mario","pasquale"]
new_user:list[str]=["amin","peppe","nicola","totti","luigi"]
current_user_lower:list[str]=[utente.lower() for utente in current_user]
current_user_upper:list[str]=[utente.upper() for utente in current_user]
utenti_eliminati:list[str]=[]

i:int=0
for utente in new_user :
    if utente in  current_user or  utente in current_user_upper or  utente in current_user_lower:
        print(f"l'user {utente} e gia in uso cambialo")
        utente_cambiato: str = input("inserisci un nuovo utente : ")

        while utente_cambiato  in current_user or  utente_cambiato in current_user_upper or  utente_cambiato in current_user_lower:
            utente_cambiato: str = input(f"hai inserito un user gia presente cambialo : ")
        utenti_eliminati.append(new_user[i])
        new_user[i]= utente_cambiato

    if utente not in current_user:
        print(f"l'utente {utente} è disponibile ")

    i+=1
print(f"gli utenti ammessi sono {new_user} \nmentre quelli eliminati sono : {utenti_eliminati} \n")


"""5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list,
 such as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.
• Store the numbers 1 through 9 in a list.
• Loop through the list.
• Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number. 
Your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th", and each result should be on a separate line."""


numeri_desinenza:dict={ "1":"st" ,  "2":"nd" ,  "3":"rd" ,  "4":"th" ,  "5":"th" ,  "6":"th" ,  "7":"th" ,  "8":"th" ,   "9":"th"}

for numero in numeri_desinenza:
    if numero == "1":
        print(f"{numero}: {numeri_desinenza[numero]}")
    elif numero =="2":
        print(f"{numero}: {numeri_desinenza[numero]}")
    elif numero == "3":
        print(f"{numero}: {numeri_desinenza[numero]}")
    else:
        print(f"{numero}: {numeri_desinenza[numero]}")