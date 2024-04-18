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