def length_of_last_word(s:str):
    s=s.strip()
    lista:list=[]
    lista=s.split(" ")
    print(lista)
    return len(lista[-1])
print(length_of_last_word(input("inserisci una frase : ")))