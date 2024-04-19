def subtract(a:int,b:int):
    res=a-b
    return res 
print(subtract(int(input()),int(input())))

def check_value(a:int):
    if a == 5:
        
        return "il numero è uguale"
    elif a>5:
         return "il numero è maggiore"
    else :
        return "il numero è minore"
print(check_value(int(input("inserisci un numero intero "))))

def check_lenght(frase:str):
    a=[]
    for l in frase:
        a.append(l)
    if len(a)==10:
             return "è uguale"
    elif len(a)>10:
         return "è maggiore"
    else :
        return "è minore"
print(check_lenght(input("inserisci la frase: ")))

def print_number(elementi:list):
     for e in elementi:
          print(e)
print_number([1,2,3,4,5,6,7,8,9])

def check_each(numbers:list):
     for n in numbers:
        if n == 5:
               print(f"{n} é uguale a 5 ")
        elif n>5:
             print(f"{n} é maggiore di 5")
        else:
             print(f"{n} è minore di 5")
check_each([1,2,3,4,5,6,7,8,9])