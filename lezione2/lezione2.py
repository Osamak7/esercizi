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