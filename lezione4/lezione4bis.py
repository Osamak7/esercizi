def is_palindromo(x:str)->bool:
    i:int=0
    r="".join(reversed(x))
    if x== r:
        return True
    else:
        return False 
    
print(is_palindromo(input("inserisci un numero da controllare : ")))