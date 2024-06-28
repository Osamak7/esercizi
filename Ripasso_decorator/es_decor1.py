from decorator1 import Analisi

@Analisi.tempo
def somma(n1:int , n2:int):
    print( n1+n2)

somma(2,5)

