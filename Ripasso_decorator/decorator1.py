from contextlib import contextmanager
import time
import sys

class Analisi:
    @staticmethod
    def tempo(func):
        
        def wrapper(*args):
            
            start = time.time()
            time.sleep(1)
            func(*args)
            
            print(f"Time elapsed: {time.time() - start}")
            
        return wrapper


@Analisi.tempo
def area_cerchio(raggio:float ):
    return raggio * raggio * 3.14

area_cerchio(1)

#Spiegazione di YIELD
def generatore():
    yield"A"
    yield"B"
    yield"C"

prova_generatore=generatore()
print(next(prova_generatore))
print(next(prova_generatore))
print(next(prova_generatore))


@contextmanager
def context_manager_decorator(*args):
    
    start_time:float= time.time()
    yield
    end_time:float= time.time()
    elapsed_time:float = end_time - start_time
    print(f"{elapsed_time}")



@context_manager_decorator
def area_cerchio2(raggio:float ):
    return raggio * raggio * 3.14

area_cerchio2(3)

#contatore interno di python
a=["ciao", "miao"]
b=a
print(sys.getrefcount(a)) #output numero volte in cui e presente l'elemento compreso questo