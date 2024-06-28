"""
Apro il file in caso esista altrimenti lo crea e scrive se e apreto in
modalita lettura con la funzione { nome_file.write("testo che vogliamo inserire nel file") }

"""
with open("esempio.py" , mode="w") as reader: # aperto il scrittura e ci scrivo
    reader.write("""
a="ciao"
print(a)
""")

with open("esempio.py",mode="r") as reader: # aperto il lettura e stampo il contenuto

    contenuto = reader.read()
    print(contenuto)




#Esempio con il Try-Exept

# try:
#     reader = open("esempio.txt", mode="r")
#     contenuto = reader.read()
#     print(contenuto)
# except FileNotFoundError:
#     print("Il file non è stato trovato.")
# except IOError:
#     print("Errore durante la lettura del file.")
# finally:
#     # Il file viene chiuso anche se si verifica un'eccezione
#     reader.close()
#     print("File chiuso correttamente.")



class ContextManager:
    def __enter__(self):
        print("sono nell'enter")
        return self
    
    def __exit__(self,exc_type, exc_value , traceback):

        if exc_type is not None:
            print("Eccezione")
        return False

with ContextManager() as cm: 
    print("ciao")
    print(cm) # stampo la posizione in memoria 
