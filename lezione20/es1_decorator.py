
def ciao(name:str):
    return f"Ciao {name}"

def saluta(func):
    return func("Bob")



print(saluta(ciao))

def decorator(func):

    def wrapper():
        import time
        start = time.time()

        print("prima parte")
        func()
        print(f"time eapsed- {time.time() - start}")
        
        print("seconda parte")

    return wrapper

def ciao():
    print("Ciao !")
    
ciao= decorator(ciao) # applico il decorator alla funzione ciao 
ciao() # richiamo la funzione decorata