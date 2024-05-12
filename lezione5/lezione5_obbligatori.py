""" 9-1. Restaurant: Make a class called Restaurant. The __init__() method 
for Restaurant should store two attributes: a restaurant_name and a cuisine_type.
 Make a method called describe_restaurant() that prints these two pieces of information,
   and a method called open_restaurant() that prints a message indicating that the restaurant is open.
     Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods."""
class Resturant:
    def __init__(self, resturant_name:str , cuisine_type:str ) -> None:
        self.resturant_name=resturant_name
        self.cuisine_type=cuisine_type
        

    def describe_resturant(self):
        print(f"il {self.resturant_name} e  un ristorante di cucina {self.cuisine_type}")
    
    def open_resturant(self):
        print(f"il ristorante {self.resturant_name} è aperto ")
    
resturant=Resturant("Spacca napoli","Napoletana")
print(resturant.resturant_name)
print(resturant.cuisine_type)
resturant.describe_resturant()
resturant.open_resturant()




"""9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three different instances from the class, and call describe_restaurant() for each instance."""

"""9-3. Users: Make a class called User. Create two attributes called first_name and last_name, 
and then create several other attributes that are typically stored in a user profile. Make a method 
called describe_user() that prints a summary of the user’s information. Make another method called greet_user() 
that prints a personalized greeting to the user. Create several instances representing different users, and call both methods for each user."""
class User :
    def __init__(self, first_name:str , last_name:str , sex:str ,age:int , login_attemps:int=0 ) -> None:
        self.first_name=first_name
        self.last_name=last_name
        self.sex=sex
        self.age=age
        self.login_attemps=login_attemps 
    
    def describe_user(self):
        print(f"nome ={self.first_name } cognome = {self.last_name} altre informazioni{self.age , self.sex}")
    def great_user(self):
        print(f"ciao {self.first_name} sono felice di rivederti")   
    
    def increment_login_attemps(self ):
        self.login_attemps+=1
    def reset_login_attemps(self  ):
        self.login_attemps = 0
       

utente1=User("Luigi","Mucciacci","M",22)
utente2=User("Marco","Rossi","M",26)
utente3=User("Paolo","Neri","M",35)
utente1.describe_user()
utente1.great_user()
utente2.describe_user()
utente2.great_user()
utente3.describe_user()
utente3.great_user()


"""9-4. Number Served: Start with your program from Exercise 9-1. Add an attribute
 called number_served with a default value of 0. Create an instance called restaurant 
 from this class. Print the number of customers the restaurant has served, and then change
   this value and print it again. Add a method called set_number_served() that lets you set 
   the number of customers that have been served. Call this method with a new number and print 
   the value again. Add a method called increment_number_served() that lets you increment the number 
   of customers who’ve been served. Call this method with any number you like that could represent how
     many customers were served in, say, a day of business. """

#da fare
class Ristorante:
    def __init__(self, nome_ristorante: str, tipo_cucina: str):
        self.nome_ristorante = nome_ristorante
        self.tipo_cucina = tipo_cucina
        self.numero_clienti_serviti = 0

    def descrivi_ristorante(self):
        print(f"Il ristorante {self.nome_ristorante} propone cucina di tipo {self.tipo_cucina}.")

    def set_number_served(self, numero):
        self.numero_clienti_serviti = numero

    def increment_number_served(self, incremento):
        self.numero_clienti_serviti += incremento

Mimmo = Ristorante("da Mimmo", "Mediterranea")
print(f"Numero di clienti serviti : {Mimmo.numero_clienti_serviti}")
Mimmo.set_number_served(100)
print(f"Numero di clienti serviti dopo l'impostazione: {Mimmo.numero_clienti_serviti}")
Mimmo.increment_number_served(50)
print(f"Numero di clienti serviti dopo l'incremento: {Mimmo.numero_clienti_serviti}")

"""9-5. Login Attempts: Add an attribute called login_attempts to your
 User class from Exercise 9-3. Write a method called increment_login_attempts() 
 that increments the value of login_attempts by 1. Write another method called reset_login_attempts()
   that resets the value of login_attempts to 0. Make an instance of the User class and call increment_login_attempts()
     several times. Print the value of login_attempts to make sure it was incremented properly, and then call 
     reset_login_attempts(). Print login_attempts again to make sure it was reset to 0."""

mimmo=User("Mimmo","Rossi","M",48)
for i in range(5):
    print(mimmo.login_attemps)
    mimmo.increment_login_attemps()
print(mimmo.login_attemps)
mimmo.reset_login_attemps()
print(mimmo.login_attemps)

"""9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant.
 Write a class called IceCreamStand that inherits from the Restaurant class 
 you wrote in Exercise 9-1  or Exercise 9-4. Either version of the class will work;
   just pick the one you like better. Add an attribute called flavors that stores a 
   list of ice cream flavors. Write a method that displays these flavors. Create an 
   instance of IceCreamStand, and call this method. """

class IceCreamStand(Resturant):
    def __init__(self, resturant_name: str, cuisine_type: str, sapori:list[str] ) -> None:
        super().__init__(resturant_name, cuisine_type)
        self.sapori=sapori
    def mostra_sapori(self):
        print(f"ecco la lista dei nostri migliori gusti : {self.sapori} ")
        
ristorante1=IceCreamStand("Pulcinella","gelateria",["pistacchio","caramello","oreo","giandujotto","cioccolato"])
ristorante1.mostra_sapori()


"""9-7. Admin: An administrator is a special kind of user. Write a class called
 Admin that inherits from the User class you wrote in Exercise 9-3 or Exercise 9-5.
   Add an attribute, privileges, that stores a list of strings like "can add post", 
   "can delete post", "can ban user", and so on. Write a method called show_privileges()
     that lists the administrator’s set of privileges. Create an instance of Admin, and call your method. """

class Admin(User):
    def __init__(self, first_name: str, last_name: str, sex: str, age: int , login_attemps: int = 0) -> None:
            super().__init__(first_name, last_name, sex, age, login_attemps)
            privilegi:list[str] =["può aggiungere post", "può eliminare post", "può escludere l'utente"]
            self.privilegi=privilegi
    def show_privileges(self):
        return f"ecco quali sono i tuoi privilegi da Admin : {self.privilegi}"
pluto=Admin("Pluto","Zar","m",44)
print(pluto.show_privileges())

"""9-8. Privileges: Write a separate Privileges class. 
The class should have one attribute, privileges, that stores a list of strings 
as described in Exercise 9-7. Move the show_privileges() method to this class. 
Make a Privileges instance as an attribute in the Admin class. Create a new instance 
of Admin and use your method to show its privileges."""



"""9-9. Battery Upgrade: Use the final version of electric_car.py from this section. Add a method to the Battery class called upgrade_battery(). This method should check the battery size and set the capacity to 65 if it isn’t already. Make an electric car with a default battery size, call get_range() once, and then call get_range() a second time after upgrading the battery. You should see an increase in the car’s range.

9-10. Imported Restaurant: Using your latest Restaurant class, store it in a module. Make a separate file that imports Restaurant. Make a Restaurant instance, and call one of Restaurant’s methods to show that the import statement is working properly.
9-11. Imported Admin: Start with your work from Exercise 9-8. Store the classes User, Privileges, and Admin in one module. Create a separate file, make an Admin instance, and call show_privileges() to show that everything is working correctly.
9-12. Multiple Modules: Store the User class in one module, and store the Privileges and Admin classes in a separate module. In a separate file, create an Admin instance and call show_privileges() to show that everything is still working correctly.
9-13. Dice: Make a class Die with one attribute called sides, which has a default value of 6. Write a method called roll_die() that prints a random number between 1 and the number of sides the die has. Make a 6-sided die and roll it 10 times. Make a 10-sided die and a 20-sided die. Roll each die 10 times.
9-14. Lottery: Make a list or tuple containing a series of 10 numbers and 5 letters. Randomly select 4 numbers or letters from the list and print a message saying that any ticket matching these 4 numbers or letters wins a prize.
9-15. Lottery Analysis: You can use a loop to see how hard it might be to win the kind of lottery you just modeled. Make a list or tuple called my_ticket. Write a loop that keeps pulling numbers until your ticket wins. Print a message reporting how many times the loop had to run to give you a winning ticket.
"""